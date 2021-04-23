"""Commonly used functionality
    """
from django.contrib.auth import get_user_model
from authentication.models import User


def create_super_user():
    admin = get_user_model().objects.create_superuser(
        'admin@admin.com', 'password')
    return admin
