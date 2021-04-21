from django.test import TestCase
from order.domain_objects.discipline import Discipline


class DisciplineTestCase(TestCase):

    def setUp(self) -> None:
        self.discipline = Discipline(1).discipline_category(
            'Psychology').discipline_name('Childhood Trauma')

    def test_can_instantiate_object_with_id_only(self):
        instance = Discipline(1)
        self.assertTrue(instance)

    def test_raise_error_if_user_email_empty(self):
        with self.assertRaises(ValueError):
            Discipline(None)

    def test_returns_error_message_if_user_email_empty(self):
        exception = 'Please provide the discipline id.'
        with self.assertRaisesMessage(Exception, exception):
            Discipline(None)

    def test_class_properties(self):
        self.assertTrue(hasattr(Discipline, 'discipline_category'))
        self.assertTrue(hasattr(Discipline, 'discipline_name'))

    def test_defines_a_human_readable_name(self):
        self.assertEqual(str(self.discipline), 'Childhood Trauma')
