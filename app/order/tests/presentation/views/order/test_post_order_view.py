from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from order.tests.common.base_test import OrderBaseTestCase
from order.presentation.views import PostOrderView
from order.forms import OrderForm


class PostOrderTestCase(OrderBaseTestCase):

    def setUp(self):
        super(PostOrderTestCase, self).setUp()
        self.form = {
            'topic': 'Anything mentionable is imaginable',
            'discipline': 1,
            'type_of_paper': 'essay',
            'no_of_pages': 4,
            'due_date': '2021-1-18',
            'citation': 'APA 7',
            'due_time': '0',
            'academic_level': 'AL1'
        }

    def test_view_properties(self):
        self.assertIsInstance(PostOrderView.form_class(), OrderForm)
        self.assertEqual(PostOrderView.success_url, '/accounts/profile/')
        self.assertTrue(issubclass(PostOrderView, LoginRequiredMixin))
        self.assertTrue(issubclass(PostOrderView, FormView))
        self.assertEqual(PostOrderView.permission_denied_message,
                         'You need to be logged in place an order')
        self.assertEqual(PostOrderView.template_name,
                         'registration/profile.html')

    def test_can_post_order_with_correct_details(self):
        post_request = self.client.post('/order/', self.form, follow=True)
        self.assertRedirects(post_request, '/accounts/profile/')

    def test_renames_form_object(self):
        post_request = self.client.post('/order/', self.form, follow=True)
        self.assertTrue(post_request.context['order_form'])

    def test_order_form_sets_initial_data(self):
        form_data = {
            'email': 'someuser@gmail.com',
            'academic_level': 'AL1',
            'type_of_paper': 'essay',
            'no_of_pages': 3,
            'due_date': '2021-03-22'
        }
        post_landing_page_request = self.client.post(
            '/', data=form_data, follow=True)
        self.assertEqual(post_landing_page_request.status_code, 200)
        get_request = self.client.get('/accounts/profile/')
        self.assertEqual(get_request.status_code, 200)
        order_form = get_request.context['order_form']
        self.assertEqual(
            order_form.fields['academic_level'].initial,
            form_data['academic_level']
        )
        self.assertEqual(
            order_form.fields['type_of_paper'].initial,
            form_data['type_of_paper']
        )

    def test_on_order_post_context_data_is_deleted(self):
        form_data = {
            'email': 'someuser@gmail.com',
            'academic_level': 'AL3',
            'type_of_paper': 'biography',
            'no_of_pages': 3,
            'due_date': '2021-03-22'
        }
        post_landing_page_request = self.client.post(
            '/', data=form_data, follow=True)
        self.assertEqual(post_landing_page_request.status_code, 200)
        get_request = self.client.get('/accounts/profile/')
        self.assertEqual(get_request.status_code, 200)
        order_form = get_request.context['order_form']
        self.assertEqual(
            order_form.fields['academic_level'].initial,
            form_data['academic_level']
        )
        self.assertEqual(
            order_form.fields['academic_level'].initial,
            form_data['academic_level']
        )
        post_request = self.client.post('/order/', self.form, follow=True)
        self.assertRedirects(post_request, '/accounts/profile/')
        order_form = post_request.context['order_form']()
        self.assertNotEqual(
            order_form.fields['academic_level'].initial,
            form_data['academic_level']
        )
        self.assertNotEqual(
            order_form.fields['type_of_paper'].initial,
            form_data['type_of_paper']
        )
