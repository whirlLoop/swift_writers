
"""Django admin models tests.
"""
from django.contrib.admin.sites import AdminSite
from order.tests.common.base_test import OrderBaseTestCase
from common.tests.utils import create_super_user
from order.admin import OrderAdmin, Order


class OrderAdminTestCase(OrderBaseTestCase):

    def setUp(self):
        super(OrderAdminTestCase, self).setUp()
        self.order_admin_model = OrderAdmin(
            model=Order,
            admin_site=AdminSite()
        )
        self.order_admin_model.save_model(
            obj=self.order,
            request=create_super_user(),
            form=None,
            change=None
        )

    def test_displays_selected_information_about_an_order(self):
        list_display_fields = ['topic', 'client', 'date_created']
        self.assertEqual(
            self.order_admin_model.list_display,
            list_display_fields
        )

    def test_can_filter_on_an_order(self):
        list_filter = ['topic', 'client', 'date_created', 'due_date', 'status']
        self.assertEqual(
            self.order_admin_model.list_filter,
            list_filter
        )

    def test_defines_search_field_parameters(self):
        search_fields = ['topic', 'client__email']
        self.assertEqual(
            self.order_admin_model.search_fields,
            search_fields
        )
