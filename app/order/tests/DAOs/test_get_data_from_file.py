import json
from django.test import TestCase
from order.DAOs.data_from_file import DataFromFile


class DataFromFileTestCase(TestCase):

    def setUp(self) -> None:
        self.data_from_file_instance = DataFromFile()
        return super().setUp()

    def test_object_properties(self):
        self.assertTrue(hasattr(self.data_from_file_instance, 'essays'))
        self.assertIsInstance(json.loads(
            self.data_from_file_instance.essays), list)
        self.assertTrue(
            hasattr(self.data_from_file_instance, 'academic_levels'))
        self.assertIsInstance(json.loads(
            self.data_from_file_instance.academic_levels), list)
        self.assertIsInstance(json.loads(
            self.data_from_file_instance.disciplines), list)

    def test_can_get_essays_from_file(self):
        essays = json.loads(self.data_from_file_instance.get('essays'))
        self.assertIsInstance(essays, list)
        essay = {
            'id': 2, 'essay_name':
            'annotated_bibliography', 'essay_description': '',
            'essay_category': 1,
            'essay_display_name': 'Annotated bibliography',
            'price_per_page': 11
        }
        self.assertIn(essay, essays)

    def test_can_get_academic_levels_from_file(self):
        levels = json.loads(
            self.data_from_file_instance.get('academic_levels'))
        level = {
            "id": 3,
            "academic_level_name": "AL3",
            "base_price": "2.00",
            "academic_level_display_name": "Bachelor's"
        }
        self.assertIn(level, levels)

    def test_can_get_disciplines_from_file(self):
        disciplines = json.loads(
            self.data_from_file_instance.get('disciplines'))
        discipline = {
            'id': 4,
            'discipline_category': 'Art',
            'discipline_name': 'Art History'
        }
        self.assertIn(discipline, disciplines)

    def test_returns_empty_list_if_file_error(self):
        levels = self.data_from_file_instance.get_data_from_file(
            'none/existent/filename')
        self.assertIsInstance(levels, list)
        self.assertEqual(len(levels), 0)

    def test_implements_a_delete_function(self):
        self.data_from_file_instance.delete('essays')
        self.assertEqual(self.data_from_file_instance.essays, None)
