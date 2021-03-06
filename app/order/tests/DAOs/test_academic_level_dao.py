"""Tests academic_level data access object.
"""
import json
from order.DAOs.academic_level_dao import AcademicLevelDAO
from order.domain_objects.academic_level_object import AcademicLevelObject
from order.tests.common.base_test import OrderBaseTestCase


class AcademicLevelDAOTestCase(OrderBaseTestCase):

    def setUp(self) -> None:
        super(AcademicLevelDAOTestCase, self).setUp()
        self.dao_instance = AcademicLevelDAO()

    def test_returns_a_list_of_academic_levels(self):
        self.assertIsInstance(
            self.dao_instance.objects, list
        )
        self.assertIsInstance(
            self.dao_instance.objects[0], AcademicLevelObject
        )
        self.assertIn(
            self.dao_instance.objects[0].academic_level_name,
            str(self.cache.get("academic_levels"))
        )
        self.assertIn(
            'College',
            str(self.cache.get("academic_levels"))
        )

    def test_provides_its_size(self):
        self.assertEqual(
            len(self.dao_instance),
            len(json.loads(self.cache.get('academic_levels')))
        )

    def test_dao_defines_an_iter_function_to_ease_iteration(self):
        self.assertTrue(hasattr(self.dao_instance, '__iter__'))
        self.assertTrue(iter(self.dao_instance))
