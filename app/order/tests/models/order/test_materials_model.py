from django.db import models
from order.tests.common.base_test import OrderBaseTestCase
from order.models import OrderMaterial
from order.models import Order


class OrderModelPropertiesTestCase(OrderBaseTestCase):

    def setUp(self) -> None:
        super(OrderModelPropertiesTestCase, self).setUp()

    def test_model_sorts_orders_by_order(self):
        ordering = OrderMaterial._meta.ordering
        self.assertEqual(ordering[0], 'order')

    def test_relation_on_delete_cascades(self):
        for f in self.order_material._meta.get_fields():
            if isinstance(f, models.ForeignKey):
                self.assertEquals(
                    f.remote_field.on_delete, models.CASCADE,
                    '{} failed, value was {}'.format(
                        f.name, f.remote_field.on_delete
                    )
                )

    def test_order_relation_is_to_order_model(self):
        model = self.order_material._meta.get_field('order').related_model
        self.assertEqual(model, Order)

    def test_defines_a_human_readable_name(self):
        self.assertIn(
            'test_material', str(self.order_material)
        )

    def test_solution_foreign_key_related_name(self):
        for f in self.order_material._meta.get_fields():
            if isinstance(f, models.ForeignKey):
                self.assertEquals(
                    f.remote_field.related_name, 'materials',
                    '{} failed, value was {}'.format(
                        f.name, f.remote_field.on_delete
                    )
                )

    def test_defines_extension_property(self):
        self.assertEqual(self.order_material.extension, '.pdf')

    def test_material_field_name(self):
        name = self.order_material._meta.get_field('material').name
        self.assertEqual(name, 'material')

    def test_material_field_upload_folder(self):
        self.assertIn(
            'orders/{}/materials/{}/'.format(self.order.client, self.order),
            self.order_material.material.name
        )
