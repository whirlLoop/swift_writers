from django.test import TestCase
from resources.utils import FetchEssays
from django_redis import get_redis_connection
import json

class FetchEssaysTestCase(TestCase):

    def setUp(self):
        self.fetch_instance = FetchEssays()
        self.cache = get_redis_connection()

    def test_fetched_essays_set_in_cache(self):
        self.fetch_instance.fetch_all()
        self.assertIsInstance(json.loads(self.cache.get("essays")), list)

    def tearDown(self):
        get_redis_connection("default").flushall()