from django.contrib.auth import get_user_model
from common.tests.base_test import BaseTestCase


class AuthBaseTestCase(BaseTestCase):

    def setUp(self):
        """Call the methods to create resources."""
        super(AuthBaseTestCase, self).setUp()

    def create_test_customer(self):
        user_model = get_user_model()
        user = user_model.objects.create_customer(
            'test@gmail.com', 'password')
        return user
