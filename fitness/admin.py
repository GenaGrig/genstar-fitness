from django.contrib import admin

from .models import RegisteredUser, Trainer, Workout

admin.site.register(RegisteredUser)

admin.site.register(Trainer)

admin.site.register(Workout)



