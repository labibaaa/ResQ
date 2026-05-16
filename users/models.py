from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Users(AbstractUser):

    ROLE_CHOICES = [
        ('Public', 'Public User'),
        ('Volunteer', 'Volunteer User'),
        ('Authority', 'Authority User'),
    ]