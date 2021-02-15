from django.test import TestCase
from order.domain_objects.essay_object import EssayObject


class EssayObjectTestCase(TestCase):

    def setUp(self) -> None:
        self.essay_object_instance = EssayObject('Annotated Bibliography', 11)
        return super().setUp()

    def test_instance_properties(self):
        self.assertTrue(hasattr(self.essay_object_instance, 'essay_name'))
        self.assertTrue(hasattr(self.essay_object_instance, 'price_per_page'))
