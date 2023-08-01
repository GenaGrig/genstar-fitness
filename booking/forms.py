from django import forms
from tempus_dominus.widgets import DateTimePicker


class BookingForm(forms.Form):
    date_time = forms.DateTimeField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"})
    )
