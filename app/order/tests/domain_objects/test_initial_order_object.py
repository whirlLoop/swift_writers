from django.test import TestCase
from order.domain_objects.initial_order import InitialOrder


class InitialOrderTestCase(TestCase):

    def setUp(self) -> None:
        self.initial_order_instance = InitialOrder('test@gmail.com')\
            .academic_level('college')\
            .essay('essay')\
            .pages(3)\
            .due_date('2021-4-7')\
            .total_cost(30)

    def test_can_instantiate_object_with_user_only(self):
        self.instance = InitialOrder('test@gmail.com')
        self.assertEqual(str(self.initial_order_instance), 'test@gmail.com')

    def test_raise_error_if_user_email_empty(self):
        with self.assertRaises(ValueError):
            InitialOrder('')

    def test_returns_error_message_if_user_email_empty(self):
        with self.assertRaisesMessage(Exception, 'User should not be empty'):
            InitialOrder('')

    def test_class_properties(self):
        self.assertTrue(hasattr(InitialOrder, 'academic_level'))
        self.assertTrue(hasattr(InitialOrder, 'essay'))
        self.assertTrue(hasattr(InitialOrder, 'due_date'))
        self.assertTrue(hasattr(InitialOrder, 'total_cost'))

    def test_defines_a_human_readable_name(self):
        self.assertEqual(str(self.initial_order_instance), 'test@gmail.com')
