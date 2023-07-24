from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
    path('membership/', views.MembershipView.as_view(), name='membership'),
    path('workouts/', views.WorkoutsView.as_view(), name='workouts'),
    path('personal_trainer/', views.PersonalTrainerView.as_view(), name='personal_trainer'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    # path('profile/', views.ProfileView.as_view(), name='profile'),
]
