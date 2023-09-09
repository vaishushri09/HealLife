# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django import forms
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'gender', 'contact_no', 'blood_group', 'weight_kg', 'height_cm', 'profile_image']

    # Add a widget to customize the profile image input field
    widgets = {
        'profile_image': forms.FileInput(attrs={'class': 'form-control-file'}),
    }

       