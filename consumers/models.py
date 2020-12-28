from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone


class ConsumerManager(BaseUserManager):
    def _create_user(self, email, password1, password2, **extra_fields):
        email = self.normalize_email(email)
        if password1 != password2:
            raise ValueError("Passwords are not confirmed!")
        user = self.model(email=email, **extra_fields)
        user.set_password(password1)
        user.save(using=self._db)
        return user

    def create_user(self, email, password1=None, password2=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(
            email=email, password1=password1, password2=password2, **extra_fields
        )

    def create_superuser(self, email, password1=None, password2=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self._create_user(
            email=email, password1=password1, password2=password2, **extra_fields
        )


class Consumer(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=80, blank=True, null=True)
    last_name = models.CharField(max_length=80, blank=True, null=True)
    phone = models.CharField(max_length=11)

    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
    password_confirm = models.CharField(max_length=254)

    birth_date = models.DateField(blank=True, null=True)
    profile = models.ImageField(upload_to="profile/", blank=True, null=True)
    bio = models.CharField(max_length=150, blank=True, null=True)

    website = models.URLField(max_length=254, blank=True, null=True)
    instagram = models.CharField(max_length=254, blank=True, null=True)
    twitter = models.CharField(max_length=254, blank=True, null=True)
    linkedin = models.CharField(max_length=254, blank=True, null=True)
    telegram = models.CharField(max_length=254, blank=True, null=True)
    youtube = models.CharField(max_length=254, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = ConsumerManager()
