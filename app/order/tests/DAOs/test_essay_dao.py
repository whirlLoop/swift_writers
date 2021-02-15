"""Tests essay data access object.
"""
import json
from django.test import TestCase
from django.conf import settings
from django_redis import get_redis_connection
from order.DAOs.essay_dao import EssayDAO
from order.domain_objects.essay_object import EssayObject


class EssayDAOTestCase(TestCase):

    def setUp(self) -> None:
        get_redis_connection("default").flushall()
        self.cache = get_redis_connection()
        root_dir = str(settings.BASE_DIR)[:-13]
        json_file_path = root_dir + 'order/tests/data/essays.json'
        with open(json_file_path) as f:
            data = json.loads(f.read())
            self.cache.set('essays', json.dumps(data))
        self.dao_instance = EssayDAO()
        return super().setUp()

    def test_returns_a_list_of_essays(self):
        self.assertIsInstance(
            self.dao_instance.get_essays(), list
        )
        self.assertIsInstance(
            self.dao_instance.get_essays()[0], EssayObject
        )
        self.assertIn(
            self.dao_instance.get_essays()[0].essay_name,
            str(self.cache.get("essays"))
        )
        self.assertIn(
            'Argumentative essay',
            str(self.cache.get("essays"))
        )

    def tearDown(self):
        get_redis_connection("default").flushall()
