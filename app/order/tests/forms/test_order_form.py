"""Test place order form.
"""
import json
from django.test import TestCase
from django.conf import settings
from django import forms
from django_redis import get_redis_connection
from order.forms import OrderInitializationForm
from order.DAOs.essay_dao import EssayDAO
from order.DAOs.academic_level_dao import AcademicLevelDAO


class OrderInitializationFormTestCase(TestCase):

    def setUp(self) -> None:
        self.root_dir = str(settings.BASE_DIR)[:-13]
        self.form = self.initialize_form()
        self.email_data = {
            "email": "test@gmail.com",
            "subject": "Order Confirmation",
            "message": "Congrats! we have received your order, please "
            "click the link below to finish the process, see you soon!"
        }
        return super().setUp()

    def initialize_form(self):
        cache = get_redis_connection()
        cache.set('essays', json.dumps(
            self.get_data_from_json_file('order/tests/data/essays.json')))
        cache.set('academic_levels', json.dumps(
            self.get_data_from_json_file(
                'order/tests/data/academic_levels.json')))
        form = OrderInitializationForm(
            EssayDAO().objects,
            AcademicLevelDAO().objects)
        return form

    def get_data_from_json_file(self, json_file_path):
        file_path = self.root_dir + json_file_path
        with open(file_path) as f:
            data = json.loads(f.read())
        return data

    def test_has_client_email_field(self):
        self.assertTrue(self.form.fields['email'])

    def test_email_field_has_correct_properties(self):
        errors = {
            'required': 'Please provide your email'
        }
        email_input = self.form.fields['email']
        self.assertEqual(email_input.required, True)
        self.assertIn(errors['required'], email_input.error_messages.values())

    def test_has_academic_level_field(self):
        self.assertTrue(self.form.fields['academic_level'])

    def test_academic_level_field_has_correct_properties(self):
        errors = {
            'required': 'Please select your academic level'
        }
        academic_level_input = self.form.fields['academic_level']
        self.assertEqual(academic_level_input.required, True)
        self.assertIn(errors['required'],
                      academic_level_input.error_messages.values())

    def test_has_essay_field(self):
        self.assertTrue(self.form.fields['essay'])

    def test_essay_field_has_correct_properties(self):
        errors = {
            'required': 'Please select the type of essay'
        }
        essay_input = self.form.fields['essay']
        self.assertEqual(essay_input.required, True)
        self.assertIn(errors['required'], essay_input.error_messages.values())

    def test_essay_choices_correctly_rendered(self):
        choices = [(item.essay_name, item.price_per_page)
                   for item in EssayDAO()]
        essay_input = self.form.fields['essay']
        self.assertEqual(essay_input.choices, choices)

    def test_academic_level_choices_correctly_rendered(self):
        choices = [(item.base_price, item.academic_level_name)
                   for item in AcademicLevelDAO()]
        academic_level_input = self.form.fields['academic_level']
        self.assertEqual(academic_level_input.choices, choices)

    def test_has_duration_field(self):
        self.assertTrue(self.form.fields['duration'])

    def test_duration_field_has_correct_properties(self):
        errors = {
            'required': 'Please provide the duration'
        }
        duration_input = self.form.fields['duration']
        self.assertEqual(duration_input.required, True)
        self.assertIn(errors['required'],
                      duration_input.error_messages.values())

    def test_duration_choices(self):
        choices = [
            ('D1', '6 hrs'),
            ('D2', '8 hrs'),
            ('D3', '12 hrs'),
            ('D4', '18 hrs'),
            ('D5', '1 day'),
            ('D6', '2 days'),
            ('D7', '3 days'),
            ('D8', '4 days'),
            ('D9', '5 days'),
            ('D10', '6 days'),
            ('D11', '1 Week'),
            ('D12', '2 Weeks'),
            ('D13', '3 Weeks'),
            ('D14', '1 Month'),
            ('D15', 'custom'),
        ]
        duration_input = self.form.fields['duration']
        self.assertEqual(duration_input.choices, choices)

    def test_has_no_of_pages_field(self):
        self.assertTrue(self.form.fields['no_of_pages'])

    def test_no_of_pages_field_attributes(self):
        no_of_pages_input = self.form.fields['no_of_pages']
        self.assertEqual(no_of_pages_input.initial, 1)

    def test_has_total_cost_field(self):
        self.assertTrue(self.form.fields['total_cost'])

    def test_total_cost_field_properties(self):
        self.assertIsInstance(
            self.form.fields['total_cost'].widget, forms.HiddenInput)

    def tearDown(self):
        get_redis_connection("default").flushall()
