from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.mail import send_mail


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
