"""BaseTestCase
    """
from django.contrib.auth import get_user_model
from common.tests.base_test import BaseTestCase
from django_redis import get_redis_connection
from order.models import Order, OrderMaterial, TempOrderMaterial
from common.tests.base_test import image


class OrderBaseTestCase(BaseTestCase):

    def setUp(self) -> None:
        super(OrderBaseTestCase, self).setUp()
        get_redis_connection("default").flushall()
        self.cache = get_redis_connection()
        self.execute_caches()
        self.logged_in_customer = self.create_logged_in_customer()
        self.order = self.create_order()
        self.order_material = self.create_order_material()
        self.temporal_order_material = self.create_temporal_order_material()

    def create_temporal_order_material(self):
        temp_material = TempOrderMaterial.objects.create(
            client=self.logged_in_customer,
            material=image('test_material.pdf')
        )
        temp_material.save()
        return temp_material

    def create_order(self):
        order = Order.objects.create(
            client=self.logged_in_customer,
            topic='Impact of social media on businesses',
            type_of_paper='essay',
            no_of_pages=4,
            due_date='2021-1-18',
            due_time='18'
        )
        order.save()
        return order

    def create_order_material(self):
        material = OrderMaterial.objects.create(
            order=self.order,
            material=image('test_material.pdf')
        )
        material.save()
        return material

    def create_logged_in_customer(self):
        user_model = get_user_model()
        user = user_model.objects.create_customer(
            'client@gmail.com', 'password')
        user.is_active = True
        user.save()
        self.client.login(username=user, password='password')
        return user
