from django.test import TestCase
from order.domain_objects.academic_level_object import AcademicLevelObject


class AcademicLevelObjectTestCase(TestCase):

    def setUp(self) -> None:
        self.academic_level_object_instance = AcademicLevelObject('College', 2)
        return super().setUp()

    def test_instance_properties(self):
        self.assertTrue(
            hasattr(self.academic_level_object_instance, 'name'))
        self.assertTrue(
            hasattr(self.academic_level_object_instance, 'base_price'))

    def test_defines_a_human_readable_name(self):
        self.assertEqual(
            str(self.academic_level_object_instance),
            'College')
