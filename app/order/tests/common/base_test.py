"""BaseTestCase
    """
from django.contrib.auth import get_user_model
from common.tests.base_test import BaseTestCase
from django_redis import get_redis_connection
from order.models import Order


class OrderBaseTestCase(BaseTestCase):

    def setUp(self) -> None:
        super(OrderBaseTestCase, self).setUp()
        get_redis_connection("default").flushall()
        self.cache = get_redis_connection()
        self.execute_caches()
        self.order = self.create_order()
        return super().setUp()

    def create_order(self):
        user_model = get_user_model()
        user = user_model.objects.create_customer(
            'client@gmail.com', 'password')
        order = Order.objects.create(
            client=user,
            topic='Impact of social media on businesses',
            type_of_paper='essay',
            no_of_pages=4,
            due_date='2021-1-18',
            due_time='18'
        )
        order.save()
        return order
