from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('authority', 'Authority'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    nid_number = models.CharField(max_length=20, unique=True)
    contact_number = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100, blank=True)
    workplace = models.CharField(max_length=150, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.role})"