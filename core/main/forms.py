from django import forms
from .models import *


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = ["service", "staff"]
