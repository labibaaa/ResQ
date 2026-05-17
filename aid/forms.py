from django import forms
from .models import CashDonation, GoodsDonation, AidStats

UNIT_CHOICES = [
    ('kg', 'kg'),
    ('pcs', 'pcs'),
    ('liters', 'liters'),
    ('boxes', 'boxes'),
]

class CashDonationForm(forms.ModelForm):
    class Meta:
        model = CashDonation
        fields = [
            'donor_name', 'contact_number', 'bkash_number',
            'amount', 'transaction_id', 'note'
        ]

class GoodsDonationForm(forms.ModelForm):
    unit = forms.ChoiceField(choices=UNIT_CHOICES)

    class Meta:
        model = GoodsDonation
        fields = [
            'donor_name', 'contact_number', 'goods_name',
            'quantity', 'unit', 'delivery_method', 'pickup_address'
        ]
        widgets = {
            'delivery_method': forms.RadioSelect(),
        }

    def clean(self):
        cleaned_data = super().clean()
        method = cleaned_data.get('delivery_method')
        address = cleaned_data.get('pickup_address')
        if method == 'pickup' and not address:
            raise forms.ValidationError(
                'Please provide a pickup address.'
            )
        return cleaned_data

class AidStatsForm(forms.ModelForm):
    class Meta:
        model = AidStats
        fields = ['lives_saved']