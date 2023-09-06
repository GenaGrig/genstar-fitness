from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from django.contrib import messages
from django.core.mail import send_mail


class MainPageView(generic.TemplateView):
    '''Main page view'''
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        '''Get context data for main page view'''
        context = super().get_context_data(**kwargs)
        context['title'] = 'Genstar'
        return context


class MembershipView(generic.TemplateView):
    '''Membership page view'''
    template_name = 'membership.html'

    def get_context_data(self, **kwargs):
        '''Get context data for membership page view'''
        context = super().get_context_data(**kwargs)
        context['title'] = 'Membership'
        return context


class WorkoutsView(generic.TemplateView):
    '''Workouts page view'''
    template_name = 'workouts.html'

    def get_context_data(self, **kwargs):
        '''Get context data for workouts page view'''
        context = super().get_context_data(**kwargs)
        context['title'] = 'Workouts'
        return context


class PersonalTrainerView(generic.TemplateView):
    '''Personal trainer page view'''
    template_name = 'personal_trainer.html'

    def get_context_data(self, **kwargs):
        '''Get context data for personal trainer page view'''
        context = super().get_context_data(**kwargs)
        context['title'] = 'personal_trainer'
        return context


class ContactView(generic.TemplateView):
    '''Contact page view'''
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        '''Get context data for contact page view'''
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        return context


class BookingView(generic.TemplateView):
    '''Booking page view'''
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        '''Get context data for booking page view'''
        context = super().get_context_data(**kwargs)
        context['title'] = 'Booking'
        return context


def register_user(request):
    '''Register user form function'''
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Your Account Has Been Created!")
            return redirect('userPanel')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


class TermsAndConditionsView(generic.TemplateView):
    '''Terms and conditions page view'''
    template_name = 'terms-and-conditions.html'

    def get_context_data(self, **kwargs):
        '''Get context data for terms and conditions page view'''
        context = super().get_context_data(**kwargs)
        context['title'] = 'Terms and Conditions'
        return context


class PrivacyPolicyView(generic.TemplateView):
    '''Privacy policy page view'''
    template_name = 'privacy-policy.html'

    def get_context_data(self, **kwargs):
        '''Get context data for privacy policy page view'''
        context = super().get_context_data(**kwargs)
        context['title'] = 'Privacy Policy'
        return context


def contact(request):
    '''Contact form sending email'''
    if request.method == 'POST':
        user_name = request.POST['user-name']
        user_email = request.POST['user-email']
        user_message = request.POST['user-message']

        # send an email
        send_mail(
            'Genstar Fitness contact from' + user_name,  # subject
            user_message,  # message
            user_email,  # from email
            ['genstarproject@gmail.com'],  # to email
            fail_silently=False,
        )

        return render(request, 'contact.html', {'user_name': user_name})

    else:
        return render(request, 'contact.html', {})