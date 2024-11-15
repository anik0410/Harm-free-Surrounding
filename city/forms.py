from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=['username','email','password1','password2']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        
        fields =['complaint_type','address','area','city','pincode','landmark','info','picture']
        
        

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields =['complaint_type','info','picture','status']

class GreenInitiativeForm(forms.ModelForm):
    class Meta:
        model = GreenInitiative
        fields = ['title', 'information', 'date', 'image', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Share your initiative title'}),
            'information': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What do you plan to do?'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Where is it happening'}),

        }
class GreenInitiativeCommentForm(forms.ModelForm):
    class Meta:
        model = GreenInitiativeComment
        fields = ['personal_views']
        widgets = {
            'personal_views': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your views'}),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['person_name', 'testimonial', 'rating']
        widgets = {
            'person_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'testimonial': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your testimonial'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rating', 'min': '1', 'max': '5'}),

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

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter initiative title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter initiative description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }