"""BaseTestCase
    """
import json
from django.test import TestCase
from django.conf import settings
from django_redis import get_redis_connection


class BaseTestCase(TestCase):

    def setUp(self) -> None:
        get_redis_connection("default").flushall()
        self.cache = get_redis_connection()
        self.root_dir = str(settings.BASE_DIR)[:-13]
        return super().setUp()

    def set_cache_from_json_file(self, key, json_file_path):
        file_path = self.root_dir + json_file_path
        with open(file_path) as f:
            data = json.loads(f.read())
            self.cache.set(key, json.dumps(data))

    def tearDown(self):
        get_redis_connection("default").flushall()
