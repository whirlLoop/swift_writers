from django.test import TestCase
from resources.utils import FetchAcademicLevels
from django_redis import get_redis_connection
import json


class FetchAcademicLevelsTestCase(TestCase):

    def setUp(self):
        self.fetch_instance = FetchAcademicLevels()
        self.cache = get_redis_connection()

    def test_fetched_academic_levels_set_in_cache(self):
        self.cache.delete('academic_levels')
        self.fetch_instance.fetch_all()
        self.assertIsInstance(json.loads(
            self.cache.get("academic_levels")), list)
        self.assertIsInstance(json.loads(
            self.cache.get("academic_levels"))[0], dict)

    def tearDown(self):
        get_redis_connection("default").flushall()
