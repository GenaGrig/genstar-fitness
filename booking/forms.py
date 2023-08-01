# forms.py
from django import forms
from .models import BookingSlots


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingSlots
        fields = ['workout_type', 'date', 'time_slot']
        
        widgets = {
            'date': forms.SelectDateWidget(),
            'time_slot': forms.TimeInput(attrs={'type': 'time'}),
        }
        
        labels = {
            'workout_type': 'Workout Type',
            'date': 'Date',
            'time_slot': 'Time Slot',
        }
        
        help_texts = {
            'date': 'Select date',
            'time_slot': 'Select time',
        }
        
        error_messages = {
            'date': {
                'invalid': 'Invalid date',
            },
            'time_slot': {
                'invalid': 'Invalid time',
            },
        }
        
        # def clean(self):
        #     cleaned_data = super().clean()
        #     date = cleaned_data.get('date')
        #     time_slot = cleaned_data.get('time_slot')
        #     if date and time_slot:
        #         if date < datetime.date.today():
        #             raise forms.ValidationError("The date cannot be in the past!")
        #         if date == datetime.date.today() and time_slot < datetime.datetime.now().time():
        #             raise forms.ValidationError("The time cannot be in the past!")
        #     return cleaned_data
        #
