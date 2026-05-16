from django.db import models
from users.models import User


class GuideSection(models.Model):
    EMERGENCY_TYPES = [
        ('fire', 'Fire'),
        ('flood', 'Flood'),
        ('earthquake', 'Earthquake'),
        ('medical', 'Medical'),
        ('structural', 'Structural Collapse'),
        ('other', 'Other'),
    ]

    emergency_type = models.CharField(
        max_length=20, choices=EMERGENCY_TYPES, unique=True
    )
    title = models.CharField(max_length=150)
    dos = models.TextField(help_text="One do per line")
    donts = models.TextField(help_text="One don't per line")
    extra_info = models.TextField(blank=True)
    last_updated_by = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={'role': 'authority'}
    )
    updated_at = models.DateTimeField(auto_now=True)

    def dos_list(self):
        return [line.strip() for line in self.dos.splitlines() if line.strip()]

    def donts_list(self):
        return [line.strip() for line in self.donts.splitlines() if line.strip()]

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
