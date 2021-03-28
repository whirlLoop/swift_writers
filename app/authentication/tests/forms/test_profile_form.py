from django.test import TestCase
from authentication.forms.change_form import AvatarUpdateForm
from django.contrib.auth.forms import UserChangeForm


class LoginFormTestCase(TestCase):

    def setUp(self) -> None:
        self.form = AvatarUpdateForm()
        return super().setUp()

    def test_defines_only_required_fields(self):
        self.assertIn('avatar', self.form.fields)

    def test_overrides_django_auth_change_form(self):
        self.assertIsInstance(self.form, UserChangeForm)
