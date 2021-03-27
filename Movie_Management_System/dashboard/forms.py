from django import forms
from django.contrib.auth.models import User
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user']

