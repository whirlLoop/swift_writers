from django.views import View
from django.core import mail
from swift_writers.presentation.landing_page import LandingPageView
from order.forms import OrderInitializationForm
from common.tests.base_test import BaseTestCase


class LandingPageTestCase(BaseTestCase):

    def setUp(self):
        super(LandingPageTestCase, self).setUp()
        self.post_data = {
            'email': 'test@gmail.com',
            'academic_level': 'AL1',
            'essay': 'essay',
            'no_of_pages': 1,
            'due_date': '2021-03-22'
        }

    def test_get_home_page_view(self):
        get_landing_page_response = self.client.get('/')
        self.assertEqual(get_landing_page_response.status_code, 200)

    def test_correct_template_used(self):
        get_landing_page_response = self.client.get('/')
        self.assertTemplateUsed(
            get_landing_page_response, 'landing_page/index.html'
        )

    def test_view_properties(self):
        self.assertIsInstance(LandingPageView(), View)

    def test_order_initialization_form_in_context(self):
        get_landing_page_response = self.client.get('/')
        self.assertIsInstance(
            get_landing_page_response.context['form'],
            OrderInitializationForm)

    def test_welcome_message_added(self):
        get_landing_page_response = self.client.get('/')
        message_title = 'Works smarter not harder!'
        self.assertIn(
            message_title, get_landing_page_response.content.decode())

    def test_form_title(self):
        get_landing_page_response = self.client.get('/')
        title = 'Manage your time better!'
        self.assertIn(title, get_landing_page_response.content.decode())

    def test_posts_form_successfully(self):
        post_landing_page_response = self.client.post(
            '/', data=self.post_data, follow=True)
        self.assertRedirects(post_landing_page_response, '/', 302)
        message = list(
            post_landing_page_response.context.get('messages'))[0]
        self.assertEqual(message.tags, 'success')
        s_msg = (
            'Congratulations, we\'ve got your paper! We\'ve sent you a link '
            'in your email with the final steps. cheers.')
        self.assertTrue('{}'.format(s_msg) in message.message)

    def test_un_successful_post_error_message(self):
        self.post_data['no_of_pages'] = -1
        post_landing_page_response = self.client.post(
            '/', data=self.post_data, follow=True)
        message = list(
            post_landing_page_response.context.get('messages'))[0]
        self.assertEqual(message.tags, 'error')
        s_msg = ('Please correct the errors in the form below')
        self.assertTrue('{}'.format(s_msg) in message.message)

    def test_email_confirmation_email_sent(self):
        self.client.post(
            '/', data=self.post_data)
        self.assertEqual(len(mail.outbox), 1)
