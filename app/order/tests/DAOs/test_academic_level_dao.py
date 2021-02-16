"""Tests academic_level data access object.
"""
from order.DAOs.academic_level_dao import AcademicLevelDAO
from order.domain_objects.academic_level_object import AcademicLevelObject
from order.tests.common.base_test import BaseTestCase


class AcademicLevelDAOTestCase(BaseTestCase):

    def setUp(self) -> None:
        super(AcademicLevelDAOTestCase, self).setUp()
        self.set_cache_from_json_file(
            'academic_levels', 'order/tests/data/academic_levels.json')
        self.dao_instance = AcademicLevelDAO()

    def test_returns_a_list_of_academic_levels(self):
        self.assertIsInstance(
            self.dao_instance.get_academic_levels(), list
        )
        self.assertIsInstance(
            self.dao_instance.get_academic_levels()[0], AcademicLevelObject
        )
        self.assertIn(
            self.dao_instance.get_academic_levels()[0].academic_level_name,
            str(self.cache.get("academic_levels"))
        )
        self.assertIn(
            'College',
            str(self.cache.get("academic_levels"))
        )
