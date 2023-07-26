from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

SERVICE_CHOICES = (
    ("BODYATTACK", "BODYATTACK"),
    ("BODYBALANCE", "BODYBALANCE"),
    ("BODYCOMBAT", "BODYCOMBAT"),
    ("BODYPUMP", "BODYPUMP"),
    ("BODYSTEP", "BODYSTEP"),
    ("Personal Trainer", "Personal Trainer"),
    ("Yoga", "Yoga"),
    )
TIME_CHOICES = (
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
    ("19:00", "19:00"),
    ("20:00", "20:00"),
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="BODYATTACK")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="10:00")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"