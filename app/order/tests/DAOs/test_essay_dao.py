"""Tests essay data access object.
"""
import json
from order.DAOs.essay_dao import EssayDAO
from order.domain_objects.essay_object import EssayObject
from order.tests.common.base_test import OrderBaseTestCase


class EssayDAOTestCase(OrderBaseTestCase):

    def setUp(self) -> None:
        super(EssayDAOTestCase, self).setUp()
        self.dao_instance = EssayDAO()

    def test_returns_a_list_of_essays(self):
        self.assertIsInstance(
            self.dao_instance.objects, list
        )
        self.assertIsInstance(
            self.dao_instance.objects[0], EssayObject
        )
        self.assertIn(
            self.dao_instance.objects[0].essay_name,
            str(self.cache.get("essays"))
        )
        self.assertIn(
            'Argumentative essay',
            str(self.cache.get("essays"))
        )

    def test_provides_its_size(self):
        self.assertEqual(
            len(self.dao_instance),
            len(json.loads(self.cache.get('essays')))
        )

    def test_dao_defines_an_iter_function_to_ease_iteration(self):
        self.assertTrue(hasattr(self.dao_instance, '__iter__'))
        self.assertTrue(iter(self.dao_instance))
