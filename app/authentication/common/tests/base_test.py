from shutil import rmtree
from django.test import TestCase
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from core.settings.base import BASE_DIR


class AuthBaseTestCase(TestCase):

    def setUp(self):
        """Call the methods to create resources."""
        self.media_url = settings.MEDIA_URL
        images_directory = str(settings.BASE_DIR) + \
            self.media_url + 'authentication/'
        rmtree(images_directory, ignore_errors=True)


def image(name):
    """
    Create an image.
    Parameters:
        name(str): name of the image
    Returns:
        image
    """
    image_path = str(BASE_DIR) + '/media/' + name
    mock_image = SimpleUploadedFile(
        name=name,
        content=open(image_path, 'rb').read(),
        content_type='image/jpeg'
    )
    return mock_image
