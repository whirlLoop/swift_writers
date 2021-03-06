from datetime import date
from django import forms
from django_mysql.forms import SimpleListField
from order.tests.common.base_test import OrderBaseTestCase
from order.forms import OrderForm
from order.models import Order, TempOrderMaterial


class OrderFormTestCase(OrderBaseTestCase):

    def setUp(self) -> None:
        self.form = OrderForm()
        self.form_data = {
            'topic': 'Social Media Marketing',
            'type_of_paper': 'essay',
            'no_of_pages': 4,
            'due_date': '2021-1-18',
            'due_time': '18',
            'academic_level': 'AL1',
            'discipline': '1',
            'citation': 'APA 7'
        }
        return super(OrderFormTestCase, self).setUp()

    def test_specifies_fields(self):
        fields = [
            'topic', 'type_of_paper',
            'no_of_pages', 'words', 'due_date', 'due_time',
            'academic_level', 'citation', 'discipline', 'description',
        ]
        self.assertEqual(self.form.Meta.fields, fields)

    def test_specifies_model(self):
        self.assertIsInstance(self.form.Meta.model(), Order)

    def test_topic_input_defines_a_placeholder(self):
        self.assertEqual(
            self.form.fields['topic'].widget.attrs['placeholder'],
            'Tell us the topic.'
        )

    def test_words_instead_input_defines_a_placeholder(self):
        self.assertEqual(
            self.form.fields['words'].widget.attrs['placeholder'],
            'Tell us the number of words.'
        )

    def test_due_date_field_has_correct_properties(self):
        due_date_input = self.form.fields['due_date']
        self.assertEqual(
            due_date_input.widget.attrs['min'], date.today()
        )
        self.assertEqual(
            due_date_input.widget.attrs['placeholder'], 'Select due date.'
        )

    def test_description_input_defines_a_placeholder(self):
        self.assertEqual(
            self.form.fields['description'].widget.attrs['placeholder'],
            'Describe what you need our writers to do. Add any other '
            'information you think might be useful'
        )

    def validates_valid_form(self):
        self.form(self.form_data)
        self.assertTrue(self.form.is_valid())

    def test_sets_order_client_on_save(self):
        form = OrderForm(self.form_data)
        request = self.client.get("/")
        request.FILES = {}
        request.user = self.logged_in_customer
        self.assertTrue(form.is_valid())
        order = form.save(request)
        self.assertEqual(order.client, self.logged_in_customer)

    def test_sets_order_status_to_placed_on_save(self):
        form = OrderForm(self.form_data)
        request = self.client.get("/")
        request.FILES = {}
        request.user = self.logged_in_customer
        self.assertTrue(form.is_valid())
        order = form.save(request)
        self.assertEqual(order.status, 'placed')

    def test_defines_a_materials_field(self):
        materials_field = self.form.fields['materials']
        self.assertIsInstance(
            materials_field, SimpleListField
        )

    def test_materials_field_properties(self):
        materials_field = self.form.fields['materials']
        self.assertFalse(materials_field.required)
        self.assertIsInstance(materials_field.widget, forms.HiddenInput)

    def test_saves_order_materials_on_save(self):
        self.form_data['materials'] = '{}'.format(
            self.temporal_order_material.pk)
        form = OrderForm(self.form_data)
        request = self.client.get("/")
        request.FILES = {}
        request.user = self.logged_in_customer
        self.assertTrue(form.is_valid())
        saved_order = form.save(request)
        self.assertEqual(saved_order.status, 'placed')
        order_materials = saved_order.materials.all()
        self.assertEqual(str(order_materials[0]), str(
            self.temporal_order_material.filename))

    def test_deletes_temporal_material_on_save(self):
        temp_materials = len(TempOrderMaterial.objects.all())
        self.assertTrue(temp_materials)
        self.form_data['materials'] = '{}'.format(
            self.temporal_order_material.pk)
        form = OrderForm(self.form_data)
        request = self.client.get("/")
        request.FILES = {}
        request.user = self.logged_in_customer
        self.assertTrue(form.is_valid())
        saved_order = form.save(request)
        self.assertEqual(saved_order.status, 'placed')
        new_temp_materials = len(TempOrderMaterial.objects.all())
        self.assertEqual((temp_materials - 1), new_temp_materials)

    def test_restricts_file_to_50_mb(self):
        pass
