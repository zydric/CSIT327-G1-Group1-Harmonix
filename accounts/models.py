from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('musician', 'Musician'),
        ('band', 'Band'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)