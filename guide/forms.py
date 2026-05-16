from django import forms
from .models import GuideSection

class GuideSectionForm(forms.ModelForm):
    class Meta:
        model = GuideSection
        fields = ['emergency_type', 'title', 'dos', 'donts', 'extra_info']