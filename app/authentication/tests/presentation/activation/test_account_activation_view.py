from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from authentication.token import account_activation_token
from authentication.common.tests.base_test import AuthBaseTestCase


class AccountActivationTestCase(AuthBaseTestCase):

    def setUp(self) -> None:
        super(AccountActivationTestCase, self).setUp()

    def test_successful_activation_redirects_to_login(self):
        user = self.create_test_customer()
        token = account_activation_token.make_token(user)
        self.assertTrue(token)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        self.assertTrue(uid)
        activation_request = self.client.get(
            '/activate/{}/{}/'.format(uid, token))
        self.assertRedirects(activation_request, '/accounts/login/', 302)

    def test_activation_failure_redirects_to_error_page(self):
        token = 'atokenthatshouldntexist'
        uid = 'NaN'
        activation_request = self.client.get(
            '/activate/{}/{}/'.format(uid, token))
        self.assertTemplateUsed(
            activation_request, 'registration/account_activation_invalid.html')
