from shutil import rmtree
from django.conf import settings
from django.contrib.auth import get_user_model
from common.tests.base_test import BaseTestCase


class AuthBaseTestCase(BaseTestCase):

    def setUp(self):
        """Call the methods to create resources."""
        self.media_url = settings.MEDIA_URL
        images_directory = str(settings.BASE_DIR) + \
            self.media_url + 'authentication/'
        rmtree(images_directory, ignore_errors=True)

    def test_customer(self):
        user_model = get_user_model()
        user = user_model.objects.create_customer(
            'test@gmail.com', 'password')
        return user
