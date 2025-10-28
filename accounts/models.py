from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


# ============================
# Custom User Manager
# ============================
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, role='musician'):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password, role='admin')
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# ============================
# User Table
# ============================
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('musician', 'Musician'),
        ('band', 'Band Admin'),
        ('admin', 'Administrator'),
    ]

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='musician')
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=50)
    location = models.CharField(max_length=100, blank=True, null=True)
    genres = models.CharField(max_length=200, blank=True, null=True)
    instruments = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)       
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"{self.username} ({self.role})"

    # Helper properties
    @property
    def is_musician(self):
        return self.role == 'musician'

    @property
    def is_band_admin(self):
        return self.role == 'band'


# ============================
# Musician Table
# ============================
class Musician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='musician_profile')
    bio = models.TextField(blank=True)
    instruments = models.CharField(max_length=255, blank=True)
    genres = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Musician: {self.user.username}"


# ============================
# Band Table
# ============================
class Band(models.Model):
    band_name = models.CharField(max_length=255)
    members = models.ManyToManyField(Musician, related_name='bands')
    genre = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.band_name
