from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('user-panel', views.userPanel, name='userPanel'),
    path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    (path('user-update-submit/<int:id>', views.userUpdateSubmit,
          name='userUpdateSubmit')),
    path('staff-panel', views.staffPanel, name='staffPanel'),
    path('delete_booking/<int:id>', views.delete_booking, name='delete'),
    (path('delete_booking_staff/<int:id>', views.delete_booking_staff,
          name='delete_staff')),
    path('update_profile/', views.update_profile, name='update_profile'),
]
