"""Test the redis config
"""
from unittest import TestCase
from redis_config import get_redis_connection


class RedisConfigTestCase(TestCase):

    def setUp(self):
        self.connection = get_redis_connection()

    def test_returns_a_connection(self):
        self.assertTrue(self.connection)
