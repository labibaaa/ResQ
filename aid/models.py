from django.db import models
from users.models import User

class CashDonation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
    ]

    donor_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    bkash_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    note = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    donated_at = models.DateTimeField(auto_now_add=True)
    verified_by = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='verified_donations',
        limit_choices_to={'role': 'authority'}
    )

    def __str__(self):
        return f"{self.donor_name} — {self.amount} BDT ({self.status})"


class GoodsDonation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('scheduled', 'Pickup Scheduled'),
        ('received', 'Received'),
    ]

    DELIVERY_CHOICES = [
        ('dropoff', 'Drop-off at Office'),
        ('pickup', 'Request Pickup'),
    ]

    donor_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    goods_name = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=20)  # kg, pcs, liters, boxes
    delivery_method = models.CharField(max_length=10, choices=DELIVERY_CHOICES)
    pickup_address = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    donated_at = models.DateTimeField(auto_now_add=True)
    assigned_volunteer = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='pickup_assignments',
        limit_choices_to={'role': 'volunteer'}
    )

    def __str__(self):
        return f"{self.donor_name} — {self.goods_name} x{self.quantity} ({self.status})"


class AidStats(models.Model):
    lives_saved = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={'role': 'authority'}
    )

    class Meta:
        verbose_name = 'Aid Stats'

    def __str__(self):
        return f"Aid Stats (updated {self.updated_at})"