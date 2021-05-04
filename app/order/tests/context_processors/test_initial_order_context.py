"""Tests for InitialOrderContextProcessor object
"""
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from order.context_processors import initial_order
from order.initial_order_data_context_manager import (
    InitialOrderDataContextManager)


class InitialOrderContextProcessorTestCase(TestCase):

    def setUp(self):
        super(InitialOrderContextProcessorTestCase, self).setUp()
        self.initial_data = {
            'user': 'test@gmail.com',
            'academic_level': 'college',
            'essay': 'essay',
            'due_data': '2021-05-21',
            'total_cost': 27,
            'pages': 3
        }
        self.request = RequestFactory().get('/')
        middleware = SessionMiddleware()
        middleware.process_request(self.request)
        self.request.session.save()
        self.initial_order_context_processor = initial_order(self.request)
        self.initial_order_context_processor.get(
            'initial_order').set_initial_order_data_to_context(
                self.initial_data)
        self.initial_order_data_context_manager_data = self.initial_order_context_processor.get(
            'initial_order').initial_order_data

    def test_returns_initial_order_data_context_manager_instance(self):
        self.assertIsInstance(
            self.initial_order_context_processor['initial_order'],
            InitialOrderDataContextManager)

    def test_context_can_be_accessed_in_templates(self):
        data = self.initial_order_data_context_manager_data
        data = data[self.initial_data['user']]
        self.assertEqual(
            data['essay'], 'essay')
        self.assertEqual(
            data['pages'], 3)
