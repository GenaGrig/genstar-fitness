from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('register/', views.RegisterView.as_view(), name='register'),
    # path('profile/', views.ProfileView.as_view(), name='profile'),
]
