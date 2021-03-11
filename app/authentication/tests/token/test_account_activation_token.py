from django.contrib.auth import get_user_model
from authentication.token import account_activation_token
from authentication.common.tests.base_test import AuthBaseTestCase


class AccountActivationTokenTestCase(AuthBaseTestCase):

    def setUp(self) -> None:
        super(AccountActivationTokenTestCase, self).setUp()

    def test_generates_token(self):
        user = get_user_model().objects.create_customer(
            'test@gmail.com', 'password')
        token = account_activation_token.make_token(user)
        self.assertTrue(token)
