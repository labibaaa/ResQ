from django.db import models
from users.models import User


class EmergencyContact(models.Model):
    CATEGORY_CHOICES = [
        ('fire', 'Fire Station'),
        ('police', 'Police'),
        ('hospital', 'Hospital'),
        ('shelter', 'Shelter'),
        ('ngo', 'NGO'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=150)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    added_by = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={'role': 'authority'}
    )

    def __str__(self):
        return f"{self.name} ({self.category})"


from django.db import models

# Create your models here.
