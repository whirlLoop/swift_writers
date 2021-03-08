import json
from django.test import TestCase
from django.conf import settings
from django_redis import get_redis_connection


class BaseTestCase(TestCase):
    """Perform common test uses
    """

    def setUp(self) -> None:
        self.root_dir = str(settings.BASE_DIR)[:-4]
        self.execute_caches()
        return super().setUp()

    def execute_caches(self):
        cache = get_redis_connection()
        cache.set('essays', json.dumps(
            self.get_data_from_json_file('order/tests/data/essays.json')))
        cache.set('academic_levels', json.dumps(
            self.get_data_from_json_file(
                'order/tests/data/academic_levels.json')))

    def get_data_from_json_file(self, json_file_path):
        file_path = self.root_dir + json_file_path
        with open(file_path) as f:
            data = json.loads(f.read())
        return data

    def tearDown(self):
        get_redis_connection("default").flushall()
