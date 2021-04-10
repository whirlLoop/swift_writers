"""Contains test for the base template.
"""
from datetime import datetime
from django.test import TestCase


class BaseTemplateTestCase(TestCase):

    def setUp(self):
        super(BaseTemplateTestCase, self).setUp()
        self.index_page_response = self.client.get('/')

    def test_template_contains_logo_container(self):
        logo = '<a class="logo" href="/">'
        self.assertIn(logo, self.index_page_response.content.decode())

    def test_template_has_site_title(self):
        title = "Swift Writers"
        self.assertInHTML(title, self.index_page_response.content.decode())

    def test_template_has_a_favicon(self):
        favicon = (
            '<link rel="shortcut icon" type="image/jpg" '
            'href="/static/resources/images/fav.png" sizes="48x48"/>'
        )
        self.assertInHTML(favicon, self.index_page_response.content.decode())

    def test_base_template_has_expected_menu_items(self):
        item_one = '<li><a href="#">How it works</a></li>'
        self.assertInHTML(item_one, self.index_page_response.content.decode())
        item_two = '<li><a href="#">Blog</a></li>'
        self.assertInHTML(item_two, self.index_page_response.content.decode())
        item_four = '<li><a href="#">Reviews</a></li>'
        self.assertInHTML(item_four, self.index_page_response.content.decode())
        item_five = (
            '<li><a href="/" class="order-btn bg-green">Order Now</a></li>')
        self.assertInHTML(item_five, self.index_page_response.content.decode())
        item_six = '<li><a href="#">Who we are</a></li>'
        self.assertInHTML(item_six, self.index_page_response.content.decode())

    def test_footer_contains_company_section(self):
        title_section = '<h4>Company</h4>'
        self.assertInHTML(
            title_section, self.index_page_response.content.decode())
        item_one = '<li><a href="#">About us</a></li>'
        self.assertInHTML(item_one, self.index_page_response.content.decode())
        item_two = '<li><a href="#">User reviews</a></li>'
        self.assertInHTML(item_two, self.index_page_response.content.decode())
        item_three = '<li><a href="#">Commonly asked questions</a></li>'
        self.assertInHTML(
            item_three, self.index_page_response.content.decode())

    def test_footer_contains_legal_section(self):
        title_section = '<h4>Legal</h4>'
        self.assertInHTML(
            title_section, self.index_page_response.content.decode())
        item_one = '<li><a href="#">Privacy policy</a></li>'
        self.assertInHTML(item_one, self.index_page_response.content.decode())
        item_two = '<li><a href="#">Cookie policy</a></li>'
        self.assertInHTML(item_two, self.index_page_response.content.decode())
        item_three = '<li><a href="#">Confidentiality policy</a></li>'
        self.assertInHTML(
            item_three, self.index_page_response.content.decode())
        item_four = '<li><a href="#">Money back guarantee</a></li>'
        self.assertInHTML(item_four, self.index_page_response.content.decode())
        item_six = '<li><a href="#">Revision policy</a></li>'
        self.assertInHTML(item_six, self.index_page_response.content.decode())

    def test_footer_contains_services_section(self):
        title_section = '<h4>Our services</h4>'
        self.assertInHTML(
            title_section, self.index_page_response.content.decode())
        message = (
            '<p>This section will contain essay categories. '
            'There will only be like five categories, the rest '
            'can be seen by clicking see more.</p>'
        )
        self.assertInHTML(message, self.index_page_response.content.decode())
        see_more_message = '<a href="#">See more >></a>'
        self.assertInHTML(
            see_more_message, self.index_page_response.content.decode())

    def test_footer_contains_contacts_section(self):
        contacts = '<h4>Contacts</h4>'
        self.assertInHTML(contacts, self.index_page_response.content.decode())
        email_address = (
            '<li><a href="mailto:pndungu54@gmail.com.com">'
            '<i class="fas fa-envelope"></i> support@swiftwriters.com</a></li>'
        )
        self.assertInHTML(
            email_address, self.index_page_response.content.decode())
        phone = ('<li><i class="fas fa-phone"></i> +1(555) 555-6677</li>')
        self.assertInHTML(phone, self.index_page_response.content.decode())
        twitter = ('<li><i class="fab fa-twitter"></i> twitter</li>')
        self.assertInHTML(twitter, self.index_page_response.content.decode())
        facebook = ('<li><i class="fab fa-facebook"></i> facebook</li>')
        self.assertInHTML(facebook, self.index_page_response.content.decode())
        instagram = ('<li><i class="fab fa-instagram"></i> instagram</li>')
        self.assertInHTML(instagram, self.index_page_response.content.decode())

    def test_footer_contains_payment_section(self):
        title_section = '<h4>We Accept:</h4>'
        self.assertInHTML(
            title_section, self.index_page_response.content.decode())
        visa = (
            '<li><a href="https://usa.visa.com/" title="Official Visa '
            'website" target="_blank"><i class="fab fa-cc-visa fa-2x">'
            '</i></a></li>'
        )
        self.assertInHTML(visa, self.index_page_response.content.decode())
        mastercard = (
            '<li><a href="https://www.mastercard.us/en-us.html" '
            'title="Official Mastercard website" target="_blank">'
            '<i class="fab fa-cc-mastercard fa-2x"></i></a></li>'
        )
        self.assertInHTML(
            mastercard, self.index_page_response.content.decode())
        paypal = (
            '<li><a href="https://www.paypal.com/us/home" title="Official '
            'PayPal website" target="_blank"><i class="fab fa-cc-paypal '
            'fa-2x"></i></a></li>')
        self.assertInHTML(paypal, self.index_page_response.content.decode())

    def test_footer_contains_disclaimer_section(self):
        message = (
            '<p><b>Disclaimer:</b> <a href="/">swiftwriters</a> is an online '
            'writing service offering custom written papers for research '
            'purposes only. The materials provided should be properly '
            'acknowledged.</p>'
        )
        self.assertInHTML(message, self.index_page_response.content.decode())

    def test_footer_contains_copyright_section(self):
        message = (
            '<p>Copyright © SwiftWriters <span id="year"></span> '
            'All Rights Reserved</p>'
        )
        self.assertInHTML(message, self.index_page_response.content.decode())
