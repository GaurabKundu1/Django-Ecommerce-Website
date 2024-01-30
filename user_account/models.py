from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    # User model representing custom user with email as the unique identifier

    # Fields for the User model
    username = models.CharField(
        max_length=150,
        validators=[UnicodeUsernameValidator, ],
        unique=True
    )
    email = models.EmailField(
        max_length=150,
        unique=True
    )
    is_staff = models.BooleanField(default=False)  # Designates whether the user can access the admin site
    is_superuser = models.BooleanField(default=False)  # Designates whether the user has all permissions
    is_active = models.BooleanField(default=True)  # Designates whether this user should be treated as active
    date_joined = models.DateTimeField(auto_now_add=True)  # Date and time when the user account was created

    # Custom manager for User model
    objects = UserManager()

    # Fields required for authentication
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", ]

    class Meta:
        ordering = ['-date_joined']  # Ordering users by date joined in descending order
