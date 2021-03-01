from django.views.generic import TemplateView
from django.test import TestCase
from swift_writers.presentation.landing_page import LandingPageView


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
        self.assertIsInstance(LandingPageView(), TemplateView)
