from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages


class MainPageView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Genstar'
        return context


class MembershipView(generic.TemplateView):
    template_name = 'membership.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Membership'
        return context


class WorkoutsView(generic.TemplateView):
    template_name = 'workouts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Workouts'
        return context


class PersonalTrainerView(generic.TemplateView):
    template_name = 'personal_trainer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'personal_trainer'
        return context
    
    
class ContactView(generic.TemplateView):
    template_name = 'contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        return context
    

# def contact(request):
#     if request.method == 'POST':
#         message_name = request.POST['message-name']
#         message_email = request.POST['message-email']
#         message = request.POST['message']
        
#         # Send an email
#         send_mail(
#             message_name,  # subject
#             message,  # message
#             message_email,  # from email
#             ['genstarproject@gmail.com'],  # to email
#             fail_silently=False,
#         )
    
#         return render(request, 'contact.html', {'message_name': message_name})
#     else:
#         return render(request, 'contact.html', {})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        # Send an email
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['genstarproject@gmail.com'],  # to email
            fail_silently=False,
        )
    
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})
    
    
class BookingView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Booking'
        return context


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Your Account Has Been Created!")
            return redirect('userPanel')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})