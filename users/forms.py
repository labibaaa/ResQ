from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'role', 'nid_number', 'contact_number',
            'occupation', 'workplace', 'date_of_birth'
        ]

    def clean_nid_number(self):
        nid = self.cleaned_data.get('nid_number')
        if User.objects.filter(nid_number=nid).exists():
            raise forms.ValidationError('This NID number is already registered.')
        return nid

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email