from django.db import models
from users.models import User

class Incident(models.Model):
    SEVERITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    EMERGENCY_TYPES = [
        ('fire', 'Fire'),
        ('flood', 'Flood'),
        ('earthquake', 'Earthquake'),
        ('medical', 'Medical'),
        ('structural', 'Structural Collapse'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('resolved', 'Resolved'),
    ]

    RESOURCE_CHOICES = [
        ('food', 'Food'),
        ('water', 'Water'),
        ('medical', 'Medical'),
        ('shelter', 'Shelter'),
        ('rescue', 'Rescue Team'),
    ]

    reporter_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_label = models.CharField(max_length=255, blank=True)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    emergency_type = models.CharField(max_length=20, choices=EMERGENCY_TYPES)
    emergency_details = models.TextField()
    resources_needed = models.JSONField(default=list, blank=True)
    people_affected = models.PositiveIntegerField(default=1)
    reporter_safe = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    assigned_volunteer = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='assigned_incidents',
        limit_choices_to={'role': 'volunteer'}
    )
    reported_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.emergency_type.upper()} — {self.reporter_name} ({self.status})"