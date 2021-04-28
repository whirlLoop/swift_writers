from django.contrib.admin.sites import AdminSite
from order.tests.common.base_test import OrderBaseTestCase
from common.tests.utils import create_super_user
from order.admin import OrderMaterial, OrderMaterialAdmin


class MaterialsAdminTestCase(OrderBaseTestCase):

    def setUp(self):
        super(MaterialsAdminTestCase, self).setUp()
        self.material_admin_model = OrderMaterialAdmin(
            model=OrderMaterial,
            admin_site=AdminSite()
        )
        self.material_admin_model.save_model(
            obj=self.order_material,
            request=create_super_user(),
            form=None,
            change=None
        )

    def test_displays_selected_information_about_an_order(self):
        list_display_fields = ['order', 'extension', 'filename']
        self.assertEqual(
            self.material_admin_model.list_display,
            list_display_fields
        )
