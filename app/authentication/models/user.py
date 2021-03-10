from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from authentication.models import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True)
    date_joined = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(
        upload_to='authentication/avatars/', null=True, blank=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
