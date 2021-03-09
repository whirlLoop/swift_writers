"""Test place order form.
"""
from datetime import date
from django.core import mail
from django.test import RequestFactory
from django.test.client import Client
from django.contrib.sites.shortcuts import get_current_site
from order.forms import OrderInitializationForm
from order.DAOs.essay_dao import EssayDAO
from order.DAOs.academic_level_dao import AcademicLevelDAO
from common.tests.base_test import BaseTestCase


class OrderInitializationFormTestCase(BaseTestCase):

    def setUp(self) -> None:
        super(OrderInitializationFormTestCase, self).setUp()
        self.form = OrderInitializationForm()
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
            'email': 'test@gmail.com',
            'academic_level': 'AL1',
            'essay': 'essay',
            'no_of_pages': 1,
            'due_date': '2021-03-22',
        }
        self.client = Client()
        self.factory = RequestFactory()
        self.request = self.factory.get("/admin/")

    def test_has_client_email_field(self):
        self.assertTrue(self.form.fields['email'])

    def test_email_field_has_correct_properties(self):
        email_input = self.form.fields['email']
        self.assertEqual(email_input.required, True)
        self.assertEqual(
            email_input.widget.attrs['placeholder'], 'Enter your email')

    def test_validates_email_provided(self):
        self.form_data['email'] = ''
        form = OrderInitializationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        error = form.errors['email'][0]
        self.assertEqual(error, 'Please provide your email.')

    def test_has_academic_level_field(self):
        self.assertTrue(self.form.fields['academic_level'])

    def test_academic_level_field_has_correct_properties(self):
        academic_level_input = self.form.fields['academic_level']
        self.assertEqual(academic_level_input.required, True)

    def test_validates_academic_level_is_provided(self):
        self.form_data['academic_level'] = ''
        form = OrderInitializationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        error = form.errors['academic_level'][0]
        self.assertEqual(
            error, 'Please select your academic level.'
        )

    def test_validates_academic_level_in_choices(self):
        self.form_data['academic_level'] = 'Non Academic Level'
        form = OrderInitializationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        error = form.errors['academic_level'][0]
        self.assertEqual(
            error,
            (
                'Select a valid choice. Non Academic Level is not one of '
                'the available choices.')
        )

    def test_has_essay_field(self):
        self.assertTrue(self.form.fields['essay'])

    def test_essay_field_has_correct_properties(self):
        essay_input = self.form.fields['essay']
        self.assertEqual(essay_input.required, True)

    def test_validates_essay_is_provided(self):
        self.form_data['essay'] = ''
        form = OrderInitializationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        error = form.errors['essay'][0]
        self.assertEqual(
            error, 'Please select the type of essay.'
        )

    def test_validates_type_of_essay_provided(self):
        self.form_data['essay'] = 'Non Essay'
        form = OrderInitializationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        error = form.errors['essay'][0]
        self.assertEqual(
            error, (
                'Select a valid choice. Non Essay is not one of the '
                'available choices.')
        )

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

    def test_has_due_date_field(self):
        self.assertTrue(self.form.fields['due_date'])

    def test_due_date_field_has_correct_properties(self):
        due_date_input = self.form.fields['due_date']
        self.assertEqual(
            due_date_input.widget.attrs['min'], date.today()
        )
        self.assertEqual(
            due_date_input.widget.attrs['placeholder'], 'Select due date'
        )
        self.assertEqual(
            due_date_input.widget.format, '%Y-%m-%d'
        )
        self.assertEqual(due_date_input.required, True)
        self.assertEqual(
            due_date_input.widget.attrs['class'], 'datepicker-input'
        )

    def test_validates_date_format(self):
        self.form_data['due_date'] = '2021-23-09'
        form = OrderInitializationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        error = form.errors['due_date'][0]
        self.assertEqual(
            error, 'Please provide a valid date format, should be yyyy-mm-dd.'
        )

    def test_validates_date_is_provided(self):
        self.form_data['due_date'] = ''
        form = OrderInitializationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        error = form.errors['due_date'][0]
        self.assertEqual(
            error, 'Please provide the due date.'
        )

    def test_has_no_of_pages_field(self):
        self.assertTrue(self.form.fields['no_of_pages'])

    def test_no_of_pages_field_attributes(self):
        no_of_pages_input = self.form.fields['no_of_pages']
        self.assertEqual(no_of_pages_input.initial, 1)
        self.assertEqual(no_of_pages_input.widget.attrs['min'], 1)

    def test_validates_no_of_pages_is_provided(self):
        self.form_data['no_of_pages'] = None
        form = OrderInitializationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        error = form.errors['no_of_pages'][0]
        self.assertEqual(
            error, 'Please provide the no of pages.'
        )

    def test_validates_no_of_pages_provided_greater_than_one(self):
        self.form_data['no_of_pages'] = -1
        form = OrderInitializationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        error = form.errors['no_of_pages'][0]
        self.assertEqual(
            error, 'Ensure number of pages is greater than or equal to 1.'
        )

    def test_sends_notification_email_to_client(self):
        form = OrderInitializationForm(data=self.form_data)
        form.data = self.form_data
        form.is_valid()
        form.send_email(self.request)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, self.email_data['subject'])
        to_email = self.form_data['email']
        self.assertEqual(mail.outbox[0].to[0], to_email)

    def test_sent_email_contains_appropriate_content(self):
        form = OrderInitializationForm(data=self.form_data)
        form.is_valid()
        form.send_email(self.request)
        self.assertEqual(len(mail.outbox), 1)
        sent_content = mail.outbox[0].alternatives[0][0]
        current_site = get_current_site(self.request)
        self.assertIn(current_site.domain + '/login', sent_content)
        self.assertIn(current_site.domain + '/profile', sent_content)
        self.assertIn(current_site.domain + '/support', sent_content)
        self.assertIn(current_site.domain + '/', sent_content)
        self.assertIn('test@gmail.com', sent_content)

    def test_email_sent_as_html(self):
        form = OrderInitializationForm(data=self.form_data)
        form.is_valid()
        form.send_email(self.request)
        self.assertEqual(len(mail.outbox), 1)
        content_type = mail.outbox[0].alternatives[0][1]
        self.assertEqual(content_type, 'text/html')

    def test_form_can_generate_password(self):
        password = self.form.generate_password()
        self.assertTrue(password)
        self.assertEqual(len(password), 12)

    def test_valid_form_ok(self):
        form = OrderInitializationForm(data=self.form_data)
        self.assertTrue(form.is_valid())
