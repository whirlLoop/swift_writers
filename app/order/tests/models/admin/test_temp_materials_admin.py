from django.contrib.admin.sites import AdminSite
from order.tests.common.base_test import OrderBaseTestCase
from common.tests.utils import create_super_user
from order.admin import TempOrderMaterial, TempOrderMaterialAdmin


class TempMaterialsAdminTestCase(OrderBaseTestCase):

    def setUp(self):
        super(TempMaterialsAdminTestCase, self).setUp()
        self.temp_material_admin_model = TempOrderMaterialAdmin(
            model=TempOrderMaterial,
            admin_site=AdminSite()
        )
        self.temp_material_admin_model.save_model(
            obj=self.temporal_order_material,
            request=create_super_user(),
            form=None,
            change=None
        )

    def test_displays_selected_information_about_an_order(self):
        list_display_fields = ['client', 'material']
        self.assertEqual(
            self.temp_material_admin_model.list_display,
            list_display_fields
        )
