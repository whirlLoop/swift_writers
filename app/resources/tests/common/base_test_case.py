"""Sets up commonly used code.
"""
from django.test import TestCase
from django_redis import get_redis_connection


class BaseTestCase(TestCase):
    def setUp(self):
        self.cache = get_redis_connection()

    def tearDown(self):
        get_redis_connection("default").flushall()
