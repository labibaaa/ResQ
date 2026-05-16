# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'role', 'nid_number', 'contact_number',
            'occupation', 'workplace', 'date_of_birth'
        ]