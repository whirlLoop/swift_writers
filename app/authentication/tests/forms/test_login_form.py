from django.test import TestCase
from django.contrib.auth.forms import UsernameField
from authentication.forms.login_form import LoginForm


class LoginFormTestCase(TestCase):

    def setUp(self) -> None:
        self.form = LoginForm()
        return super().setUp()

    def test_username_field_is_usernamefield(self):
        username_field = self.form.fields['username']
        self.assertIsInstance(username_field, UsernameField)

    def test_username_field_attributes(self):
        username_field = self.form.fields['username']
        self.assertEqual(
            username_field.widget.attrs['placeholder'], 'Enter your email')
        self.assertEqual(
            username_field.widget.attrs['autofocus'], True)
