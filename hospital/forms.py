from django import forms
from django.forms import ModelForm
from .models import Service,Doctor

class ServiceForm(ModelForm):
    class Meta:
        model=Service
        fields= '__all__'

class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"