from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from django.contrib import messages
from django.core.mail import send_mail


class MainPageView(generic.TemplateView):
    '''Main page view.'''
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Genstar'
        return context


class MembershipView(generic.TemplateView):
    '''Membership page view.'''
    template_name = 'membership.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Membership'
        return context


class WorkoutsView(generic.TemplateView):
    '''Workouts page view.'''
    template_name = 'workouts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Workouts'
        return context


class PersonalTrainerView(generic.TemplateView):
    '''Personal Trainer page view.'''
    template_name = 'personal_trainer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'personal_trainer'
        return context


class ContactView(generic.TemplateView):
    '''Contact page view.'''
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        return context


class BookingView(generic.TemplateView):
    '''Booking page view.'''
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Booking'
        return context


def register_user(request):
    '''Register new user form.'''
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Your Account Has Been Created!")
            return redirect('userPanel')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


class TermsAndConditionsView(generic.TemplateView):
    '''Terms and Conditions page view.'''
    template_name = 'terms-and-conditions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Terms and Conditions'
        return context


class PrivacyPolicyView(generic.TemplateView):
    '''Privacy Policy page view.'''
    template_name = 'privacy-policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Privacy Policy'
        return context


def contact(request):
    '''Contact page form.'''
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


def PageNotFoundView(request):
    '''404 Page not found'''
    return render(request, '404.html', {})
