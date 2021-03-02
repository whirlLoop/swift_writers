from django.views.generic import TemplateView
from django.views import View
from django.test import TestCase
from swift_writers.presentation.landing_page import LandingPageView
from order.forms import OrderInitializationForm


class LandingPageTestCase(TestCase):

    def setUp(self):
        super(LandingPageTestCase, self).setUp()
        self.landing_page_response = self.client.get('/')

    def test_home_page_view(self):
        self.assertEqual(self.landing_page_response.status_code, 200)

    def test_correct_template_used(self):
        self.assertTemplateUsed(
            self.landing_page_response, 'landing_page/index.html'
        )

    def test_view_properties(self):
        self.assertIsInstance(LandingPageView(), View)

    def test_order_initialization_form_in_context(self):
        self.assertIsInstance(
            self.landing_page_response.context['form'],
            OrderInitializationForm)

    def test_welcome_message_added(self):
        message_title = 'Save your time for yourself!'
        message = (
            'use our service to create time for other important issues on '
            'your busy schedule, score better grades and balance your '
            'academic life. And unlike other services, we actually care '
            'about your budget.'
        )
        self.assertIn(
            message_title, self.landing_page_response.content.decode())
        self.assertContains(self.landing_page_response, message)

    def test_form_title(self):
        title = 'Manage your time better!'
        self.assertIn(title, self.landing_page_response.content.decode())
