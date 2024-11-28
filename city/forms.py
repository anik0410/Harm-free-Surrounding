from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']


import requests
from django.core.exceptions import ValidationError


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint_type', 'address', 'city', 'postal_code', 'info', 'picture', 'video']

    # No need for geocoding in the form. Just validate the form fields as usual
    def clean(self):
        cleaned_data = super().clean()
        address = cleaned_data.get("address")
        city = cleaned_data.get("city")
        postal_code = cleaned_data.get("postal_code")

        # Optional validation for empty fields (if necessary)
        if not address or not city or not postal_code:
            raise forms.ValidationError("Address, city, and postal code are required.")

        return cleaned_data


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint_type', 'info', 'picture', 'status']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['person_name', 'testimonial', 'rating']
        widgets = {
            'person_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'testimonial': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your testimonial'}),
            'rating': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Rating', 'min': '1', 'max': '5'}),

        }


class QueryForm(forms.ModelForm):
    class Meta:
        model = Queries
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Your Query'}),
        }