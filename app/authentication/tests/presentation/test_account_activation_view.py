from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from authentication.token import account_activation_token
from common.tests.base_test import BaseTestCase


class AccountActivationTestCase(BaseTestCase):

    def setUp(self) -> None:
        super(AccountActivationTestCase, self).setUp()
        self.post_data = {
            'email': 'test@gmail.com',
            'academic_level': 'AL1',
            'essay': 'essay',
            'no_of_pages': 1,
            'due_date': '2021-03-22'
        }

    def test_successful_activation_redirects_to_login(self):
        user_model = get_user_model()
        user = user_model.objects.create_customer(
            'test@gmail.com', 'password')
        token = account_activation_token.make_token(user)
        self.assertTrue(token)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        self.assertTrue(uid)
        activation_request = self.client.get(
            '/activate/{}/{}/'.format(uid, token))
        self.assertRedirects(activation_request, '/login', 302)

    def test_activation_failure_redirects_to_error_page(self):
        token = 'atokenthatshouldntexist'
        uid = 'NaN'
        activation_request = self.client.get(
            '/activate/{}/{}/'.format(uid, token))
        self.assertTemplateUsed(
            activation_request, 'registration/account_activation_invalid.html')
