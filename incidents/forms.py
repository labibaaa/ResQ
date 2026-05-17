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

    reporter_safe = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'id': 'id_reporter_safe'})
    )

    emergency_details = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Describe what is happening, how many people are involved, and any other relevant details...'
        })
    )

    class Meta:
        model = Incident
        fields = [
            'reporter_name', 'contact_number',
            'latitude', 'longitude', 'location_label',
            'severity', 'emergency_type', 'emergency_details',
            'resources_needed', 'people_affected', 'reporter_safe'
        ]