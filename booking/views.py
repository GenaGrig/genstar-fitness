from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
from .forms import MyUserChangeForm
from django.contrib.auth.models import User


def workout_view(request):
    '''Display all workouts in the database'''
    context = {
        'all_workouts': Appointment.objects.filter(foo='bar').order_by('workout').all
        }
    return render(request, 'booking.html', context=context)


def index(request):
    return render(request, "index.html", {})


def booking(request):
    # Calling 'validWeekday' Function to Loop days you want in the next 30 days:
    weekdays = validWeekday(30)

    # Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        workout = request.POST.get('workout')
        day = request.POST.get('day')
        if workout is None:
            messages.success(request, "Please Select A Workout!")
            return redirect('booking')

        # Store day and service in django session:
        request.session['day'] = day
        request.session['workout'] = workout

        return redirect('bookingSubmit')

    return render(request, 'booking.html', {
            'weekdays': weekdays,
            'validateWeekdays': validateWeekdays,
        })


def bookingSubmit(request):
    '''Save a booking to the database'''
    user = request.user
    times = [
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
        "18:00",
        "19:00",
        "20:00"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=30)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    # Get stored data from django session:
    day = request.session.get('day')
    workout = request.session.get('workout')

    # Only show the time of the day that has not been selected before:
    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if workout is not None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Tuesday' or date == 'Wednesday' or date == 'Thursday' or date == 'Friday' or date == 'Saturday' or date == 'Sunday':
                    if Appointment.objects.filter(day=day).count() < 30:
                        if Appointment.objects.filter(day=day, time=time).count() < 30:
                            AppointmentForm = Appointment.objects.get_or_create(
                                user=user,
                                workout=workout,
                                day=day,
                                time=time,
                            )
                            messages.success(request, "Booking Saved!")
                            return redirect('userPanel')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Workout!")

    return render(request, 'bookingSubmit.html', {
        'times': hour,
    })


def userPanel(request):
    '''Display all bookings for the current user'''
    user = request.user
    appointments = Appointment.objects.filter(user=user).order_by('day', 'time')
    return render(request, 'userPanel.html', {
        'user': user,
        'appointments': appointments,
    })


def userUpdate(request, id):
    '''Update a booking in the database'''
    appointment = Appointment.objects.get(pk=id)
    userdatepicked = appointment.day
    # Copy  booking:
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    # 24h if statement in template:
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(days=30)).strftime('%Y-%m-%d')
    # Calling 'validWeekday' Function to Loop days you want in the next 30 days:
    weekdays = validWeekday(30)

    # Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        workout = request.POST.get('workout')
        day = request.POST.get('day')
        if workout is None:
            messages.success(request, "Please Select A Workout!")
            return redirect('userUpdate', id=id)

        # Store day and service in django session:
        request.session['day'] = day
        request.session['workout'] = workout

        return redirect('userUpdateSubmit', id=id)

    return render(request, 'userUpdate.html', {
            'weekdays': weekdays,
            'validateWeekdays': validateWeekdays,
            'delta24': delta24,
            'id': id,
        })


def userUpdateSubmit(request, id):
    '''Save am updated booking to the database'''
    user = request.user
    times = [
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
        "18:00",
        "19:00",
        "20:00"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=30)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    workout = request.session.get('workout')

    # Only show the time of the day that has not been selected before and
    # the time he is editing:
    hour = checkEditTime(times, day, id)
    appointment = Appointment.objects.get(pk=id)
    userSelectedTime = appointment.time
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if workout is not None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Tuesday' or date == 'Wednesday' or date == 'Thursday' or date == 'Friday' or date == 'Saturday' or date == 'Sunday':
                    if Appointment.objects.filter(day=day).count() < 30:
                        if Appointment.objects.filter(day=day, time=time).count() < 30 or userSelectedTime == time:
                            appointment = Appointment.objects.filter(pk=id).update(
                                user=user,
                                workout=workout,
                                day=day,
                                time=time,
                            )
                            messages.success(request, "Booking Edited!")
                            return redirect('userPanel')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Workout!")
        return redirect('userPanel')

    return render(request, 'userUpdateSubmit.html', {
        'times': hour,
        'id': id,
    })


def staffPanel(request):
    '''Display all bookings for all users to staff members'''
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=30)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    # Only show the Appointments 30 days from today
    items = Appointment.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'time')

    return render(request, 'staffPanel.html', {
        'items': items,
    })


def dayToWeekday(x):
    '''Convert a date to a day of the week'''
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):
    # Loop days you want in the next 30 days:
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Tuesday' or y == 'Wednesday' or y == 'Thursday' or y == 'Friday' or y == 'Saturday' or y == 'Sunday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def isWeekdayValid(x):
    '''Only show the days that are not full'''
    validateWeekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 30:
            validateWeekdays.append(j)
    return validateWeekdays


def checkTime(times, day):
    # Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 30:
            x.append(k)
    return x


def checkEditTime(times, day, id):
    # Only show the time of the day that has not been selected before:
    x = []
    appointment = Appointment.objects.get(pk=id)
    time = appointment.time
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 30 or time == k:
            x.append(k)
    return x


def delete_booking(request, id):
    '''Delete a booking from the database by user'''
    appointment = Appointment.objects.get(pk=id)
    appointment.delete()
    messages.success(request, "Booking Deleted!")
    return redirect('userPanel')


def delete_booking_staff(request, id):
    '''Delete a booking from the database by staff member'''
    appointment = Appointment.objects.get(pk=id)
    appointment.delete()
    messages.success(request, "Booking Deleted!")
    return redirect('staffPanel')


def is_booking_allowed(workout_type, date, time_slot):
    # Count existing bookings for the given workout type, date, and time slot
    existing_bookings_count = Appointment.objects.filter(
        workout_type=workout_type,
        date=date,
        time_slot=time_slot,
    ).count()

    # Set the maximum booking limit per hour for each workout type
    max_booking_limit = 20

    # Check if the booking limit has been reached
    if existing_bookings_count >= max_booking_limit:
        return False
    else:
        return True


def update_profile(request):
    '''Update a user's profile'''
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = MyUserChangeForm(request.POST or None, request.FILES or None, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile Has Been Updated!")
            return redirect('userPanel')
        return render(request, 'update_profile.html', {'form': form})
    else:
        messages.success(request, "Please Login First!")
        return redirect('account_login')
