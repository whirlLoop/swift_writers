"""Tests for InitialOrderContextProcessor object
"""
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from order.context_processors import initial_order
from order.domain_objects.initial_order import InitialOrder


class InitialOrderContextProcessorTestCase(TestCase):

    def setUp(self):
        super(InitialOrderContextProcessorTestCase, self).setUp()
        self.request = RequestFactory().get('/')
        middleware = SessionMiddleware()
        middleware.process_request(self.request)
        self.request.session.save()
        self.initial_order_context = initial_order(self.request)
        self.initial_order_context.get('initial_order')

    def test_returns_order_context_processor(self):
        order = self.initial_order_context.get(
            'initial_order')('test@gmail.com')
        self.assertIsInstance(order, InitialOrder)

    def test_cart_object_added_to_context(self):
        order = self.initial_order_context.get(
            'initial_order')('test@gmail.com')
        self.assertEqual(str(order), 'test@gmail.com')

    def test_context_can_be_accessed_in_templates(self):
        request = self.client.get('/')
        self.assertIsInstance(request.context['initial_order'](
            'test@gmail.com'), InitialOrder)
