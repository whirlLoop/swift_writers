"""Profile page form.
"""
from authentication.models import User
from django.contrib.auth.forms import UserChangeForm


class AvatarUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['avatar']

