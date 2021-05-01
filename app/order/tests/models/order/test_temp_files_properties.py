from django.db import models
from django.utils import timezone
from order.models import TempOrderMaterial
from order.tests.common.base_test import OrderBaseTestCase
from authentication.models import User


class TempOrderMaterialTestCase(OrderBaseTestCase):

    def setUp(self):
        super(TempOrderMaterialTestCase, self).setUp()

    def test_model_sorts_orders_by_date(self):
        ordering = TempOrderMaterial._meta.ordering
        self.assertEqual(ordering[0], 'date_uploaded')

    def test_temp_material_relation_is_to_user_model(self):
        model = self.temporal_order_material._meta.get_field(
            'client').related_model
        self.assertEqual(model, User)

    def test_client_field_blank_true(self):
        blank = self.temporal_order_material._meta.get_field(
            'client').blank
        self.assertTrue(blank)

    def test_client_field_null_true(self):
        null = self.temporal_order_material._meta.get_field(
            'client').null
        self.assertTrue(null)

    def test_relation_on_delete_cascades(self):
        for f in self.temporal_order_material._meta.get_fields():
            if isinstance(f, models.ForeignKey):
                self.assertEquals(
                    f.remote_field.on_delete, models.CASCADE,
                    '{} failed, value was {}'.format(
                        f.name, f.remote_field.on_delete
                    )
                )

    def test_defines_a_human_readable_name(self):
        self.assertIn(
            'test_material', str(self.temporal_order_material)
        )

    def test_foreign_key_related_name(self):
        for f in self.temporal_order_material._meta.get_fields():
            if isinstance(f, models.ForeignKey):
                self.assertEquals(
                    f.remote_field.related_name, 'temp_materials',
                    '{} failed, value was {}'.format(
                        f.name, f.remote_field.on_delete
                    )
                )

    def test_defines_material_field(self):
        name = self.temporal_order_material._meta.get_field('material').name
        self.assertEqual(name, 'material')

    def test_material_field_upload_folder(self):
        self.assertIn(
            'orders/temp_materials/{}'.format(self.order.client),
            self.temporal_order_material.material.name
        )

    def test_defines_date_uploaded_field(self):
        name = self.temporal_order_material._meta.get_field(
            'date_uploaded').name
        self.assertEqual(name, 'date_uploaded')

    def test_date_uploaded_field_defaults_to_current_timezone_date(self):
        default = self.temporal_order_material._meta.get_field(
            'date_uploaded').default
        self.assertEqual(default, timezone.now)

    def test_material_field_defines_required_custom_error(self):
        messages = self.temporal_order_material._meta.get_field(
            'material'
        ).error_messages
        material_error_messages = {
            'required': (
                'Please provide the material.'
            ),
        }
        self.assertDictContainsSubset(material_error_messages, messages)

    # def test_temp_material_directory_path(self):
    #     returned_path = temp_material_directory_path(
    #         self.logged_in_customer, self.temporal_order_material)
    #     self.assertEqual(returned_path, 'orders/temp_materials/{0}/{1}'.format(
    #         self.temporal_order_material, self.temporal_order_material))
