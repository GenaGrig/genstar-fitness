from django.shortcuts import render, redirect
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
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


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Send an email
        send_mail(
            'Message from ' + message_name,  # subject
            message_name,  # subject
            message,  # message
            'settings.EMAIL_HOST_USER',  # from email
            message_email,  # from email
            ['genstarproject@gmail.com'],  # to email
            fail_silently=False,
        )

        messages.success(request, "Your Message Has Been Sent!")
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
    template_name = 'terms-and-conditions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Terms and Conditions'
        return context


class PrivacyPolicyView(generic.TemplateView):
    template_name = 'privacy-policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Privacy Policy'
        return context
