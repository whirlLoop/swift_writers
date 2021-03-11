from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from authentication.token import account_activation_token
from authentication.common.tests.base_test import AuthBaseTestCase


class LoginTestCase(AuthBaseTestCase):

    def setUp(self) -> None:
        super(LoginTestCase, self).setUp()

    def test_successful_activation_redirects_to_login(self):
        user = self.test_customer()
        user.is_active = True
        user.save()
        form = {
            'username': user.email,
            'password': 'password'
        }
        login_request = self.client.post('/accounts/login/', data=form)
        self.assertRedirects(login_request, '/', 302)
