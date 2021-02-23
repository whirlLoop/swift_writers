"""Test place order form.
"""
from datetime import date
import json
from django.test import TestCase
from django.conf import settings
from django.core import mail
from django import forms
from django.test import RequestFactory
from django.test.client import Client
from django.contrib.sites.shortcuts import get_current_site
from django_redis import get_redis_connection
from order.forms import OrderInitializationForm
from order.DAOs.essay_dao import EssayDAO
from order.DAOs.academic_level_dao import AcademicLevelDAO


class OrderInitializationFormTestCase(TestCase):

    def setUp(self) -> None:
        self.root_dir = str(settings.BASE_DIR)[:-13]
        self.form = self.initialize_form()
        subject = (
            "Registration completed. Check your login details and "
            "finish up your order for free!"
        )
        self.email_data = {
            "subject": subject,
            "message": "Congrats! we have received your order, please "
            "click the link below to finish the process, see you soon!"
        }
        self.form_data = {
            "email": "test@gmail.com",
            "academic_level": "AL1",
            "essay": "essay",
            "duration": "2021-02-23"
        }
        self.client = Client()
        self.factory = RequestFactory()
        self.request = self.factory.get("/admin/")
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
        choices = [
            (item.essay_name, item.essay_display_name)
            for item in EssayDAO()
        ]
        essay_input = self.form.fields['essay']
        self.assertEqual(essay_input.choices, choices)

    def test_academic_level_choices_correctly_rendered(self):
        choices = [
            (item.academic_level_name, item.academic_level_display_name)
            for item in AcademicLevelDAO()
        ]
        academic_level_input = self.form.fields['academic_level']
        self.assertEqual(academic_level_input.choices, choices)

    def test_has_duration_field(self):
        self.assertTrue(self.form.fields['duration'])

    def test_duration_field_has_correct_properties(self):
        errors = {
            'required': 'Please provide the duration'
        }
        duration_input = self.form.fields['duration']
        self.assertEqual(
            duration_input.widget.attrs['min'], date.today()
        )
        self.assertEqual(duration_input.required, True)
        self.assertIn(errors['required'],
                      duration_input.error_messages.values())

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

    def test_sends_notification_email_to_client(self):
        form = OrderInitializationForm(
            EssayDAO().objects,
            AcademicLevelDAO().objects,
            data=self.form_data
        )
        form.data = self.form_data
        form.is_valid()
        form.send_email(self.request)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, self.email_data['subject'])
        to_email = self.form_data['email']
        self.assertEqual(mail.outbox[0].to[0], to_email)

    def test_sent_email_contains_appropriate_content(self):
        form = OrderInitializationForm(
            EssayDAO().objects,
            AcademicLevelDAO().objects,
            data=self.form_data
        )
        form.is_valid()
        form.send_email(self.request)
        self.assertEqual(len(mail.outbox), 1)
        sent_content = mail.outbox[0].alternatives[0][0]
        current_site = get_current_site(self.request)
        self.assertIn(current_site.domain + '/login', sent_content)
        self.assertIn(current_site.domain + '/profile', sent_content)
        self.assertIn(current_site.domain + '/support', sent_content)

    def test_email_sent_as_html(self):
        form = OrderInitializationForm(
            EssayDAO().objects,
            AcademicLevelDAO().objects,
            data=self.form_data
        )
        form.is_valid()
        form.send_email(self.request)
        self.assertEqual(len(mail.outbox), 1)
        content_type = mail.outbox[0].alternatives[0][1]
        self.assertEqual(content_type, 'text/html')

    def test_form_can_generate_password(self):
        password = self.form.generate_password()
        self.assertTrue(password)
        self.assertEqual(len(password), 12)

    def tearDown(self):
        get_redis_connection("default").flushall()
