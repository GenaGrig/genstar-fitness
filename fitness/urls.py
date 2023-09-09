from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
    path('404', views.PageNotFoundView, name='404'),
    path('membership/', views.MembershipView.as_view(), name='membership'),
    path('workouts/', views.WorkoutsView.as_view(), name='workouts'),
    path('personal_trainer/', views.PersonalTrainerView.as_view(),
         name='personal_trainer'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('register/', views.register_user, name='register'),
    path('terms-and-conditions/', views.TermsAndConditionsView.as_view(),
         name='terms-and-conditions'),
    path('privacy-policy/', views.PrivacyPolicyView.as_view(),
         name='privacy-policy'),
]
