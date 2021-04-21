"""Tests discipline data access object.
"""
import json
from order.DAOs.discipline_dao import DisciplineDAO
from order.domain_objects.discipline import Discipline
from order.tests.common.base_test import OrderBaseTestCase


class DisciplineDAOTestCase(OrderBaseTestCase):

    def setUp(self) -> None:
        super(DisciplineDAOTestCase, self).setUp()
        self.dao_instance = DisciplineDAO()

    def test_returns_a_list_of_disciplines(self):
        self.assertIsInstance(
            self.dao_instance.objects, list
        )
        self.assertIsInstance(
            self.dao_instance.objects[0], Discipline
        )
        self.assertIn(
            self.dao_instance.objects[0]._discipline_name,
            str(self.cache.get("disciplines"))
        )
        self.assertIn(
            'Art',
            str(self.cache.get("disciplines"))
        )

    def test_provides_its_size(self):
        self.assertEqual(
            len(self.dao_instance),
            len(json.loads(self.cache.get('disciplines')))
        )

    def test_dao_defines_an_iter_function_to_ease_iteration(self):
        self.assertTrue(hasattr(self.dao_instance, '__iter__'))
        self.assertTrue(iter(self.dao_instance))
