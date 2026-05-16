from django.db import models
from users.models import User

class SafeZone(models.Model):
    ZONE_TYPES = [
        ('general', 'General Shelter'),
        ('medical', 'Medical Center'),
        ('flood_safe', 'Flood-Safe Zone'),
        ('fire_safe', 'Fire-Safe Zone'),
    ]

    name = models.CharField(max_length=150)
    zone_type = models.CharField(max_length=20, choices=ZONE_TYPES)
    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    capacity = models.PositiveIntegerField(default=0)
    current_occupancy = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    added_by = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={'role': 'authority'}
    )

    def availability(self):
        return max(self.capacity - self.current_occupancy, 0)

    def is_full(self):
        return self.current_occupancy >= self.capacity

    def __str__(self):
        return f"{self.name} ({self.get_zone_type_display()})"