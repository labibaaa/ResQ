from django import forms
from .models import EmergencyContact

class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = [
            'name', 'category', 'phone_number',
            'address', 'latitude', 'longitude', 'notes', 'is_active'
        ]