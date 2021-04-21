import json
from django.test import TestCase
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django_redis import get_redis_connection
from core.settings.base import BASE_DIR


class BaseTestCase(TestCase):
    """Perform common test uses
    """

    def setUp(self) -> None:
        self.root_dir = str(settings.BASE_DIR)[:-4]
        return super().setUp()

    def execute_caches(self):
        cache = get_redis_connection()
        cache.set('essays', json.dumps(
            self.get_data_from_json_file('order/data/essays.json')))
        cache.set('academic_levels', json.dumps(
            self.get_data_from_json_file(
                'order/data/academic_levels.json')))
        cache.set('disciplines', json.dumps(
            self.get_data_from_json_file(
                'order/data/disciplines.json')))

    def get_data_from_json_file(self, json_file_path):
        file_path = self.root_dir + json_file_path
        with open(file_path) as f:
            data = json.loads(f.read())
        return data

    def tearDown(self):
        get_redis_connection("default").flushall()


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
