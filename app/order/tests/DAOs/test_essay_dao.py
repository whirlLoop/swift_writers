"""Tests essay data access object.
"""
from order.DAOs.essay_dao import EssayDAO
from order.domain_objects.essay_object import EssayObject
from order.tests.common.base_test import BaseTestCase


class EssayDAOTestCase(BaseTestCase):

    def setUp(self) -> None:
        super(EssayDAOTestCase, self).setUp()
        self.set_cache_from_json_file('order/tests/data/essays.json')
        self.dao_instance = EssayDAO()

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
