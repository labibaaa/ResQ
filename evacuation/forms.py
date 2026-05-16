from django import forms
from .models import SafeZone

class SafeZoneForm(forms.ModelForm):
    class Meta:
        model = SafeZone
        fields = [
            'name', 'zone_type', 'address',
            'latitude', 'longitude', 'capacity',
            'current_occupancy', 'is_active', 'notes'
        ]