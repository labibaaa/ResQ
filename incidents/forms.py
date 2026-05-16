from django import forms
from .models import Incident

RESOURCE_OPTIONS = [
    ('food', 'Food'),
    ('water', 'Water'),
    ('medical', 'Medical'),
    ('shelter', 'Shelter'),
    ('rescue', 'Rescue Team'),
]

class IncidentReportForm(forms.ModelForm):
    resources_needed = forms.MultipleChoiceField(
        choices=RESOURCE_OPTIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Incident
        fields = [
            'reporter_name', 'contact_number',
            'latitude', 'longitude', 'location_label',
            'severity', 'emergency_type', 'emergency_details',
            'resources_needed', 'people_affected', 'reporter_safe'
        ]
