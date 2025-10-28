from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


# ============================
# Custom User Manager
# ============================
class UserManager(BaseUserManager):
    """
    Custom manager for the User model.
    """
    def create_user(self, username, email, password=None, role='musician'):
        """
        Creates and saves a regular user.
        """
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a superuser.
        """
        # Note: Superuser role is set to 'admin' by default here
        user = self.create_user(username, email, password, role='admin')
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# ============================
# Custom User Model
# ============================
class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model replacing the default Django User.
    """
    ROLE_CHOICES = [
        ('musician', 'Musician'),
        ('band', 'Band Admin'),
        ('admin', 'Administrator'),
    ]

    # Core user fields
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='musician')
    date_joined = models.DateTimeField(default=timezone.now)

    # Profile-related fields (common to all users)
    location = models.CharField(max_length=100, blank=True, null=True)
    genres = models.CharField(max_length=200, blank=True, null=True)
    instruments = models.CharField(max_length=200, blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Permissions and status
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Required for admin access

    # Manager assignment
    objects = UserManager()

    # Field settings for authentication
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # Fields prompted when creating a superuser

    def __str__(self):
        return f"{self.username} ({self.role})"

    # --- Helper properties ---

    @property
    def is_musician(self):
        """Returns True if the user is a musician."""
        return self.role == 'musician'

    @property
    def is_band_admin(self):
        """Returns True if the user is a band admin."""
        return self.role == 'band'


# ============================
# Musician Profile Model
# ============================
class Musician(models.Model):
    """
    Stores additional information specific to Musician users.
    Links one-to-one with the User model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='musician_profile')
    bio = models.TextField(blank=True)
    
    # Note: These fields are duplicates of fields on the User model.
    # Consider if they are needed here or if the User model's fields suffice.
    instruments = models.CharField(max_length=255, blank=True)
    genres = models.CharField(max_length=255, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Musician: {self.user.username}"


# ============================
# Band Model
# ============================
class Band(models.Model):
    """
    Represents a band, which can contain multiple Musician members.
    """
    band_name = models.CharField(max_length=255)
    members = models.ManyToManyField(Musician, related_name='bands')
    genre = models.CharField(max_length=255, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.band_name