"""BaseTestCase
    """
from common.tests.base_test import BaseTestCase
from django_redis import get_redis_connection


class OrderBaseTestCase(BaseTestCase):

    def setUp(self) -> None:
        super(OrderBaseTestCase, self).setUp()
        get_redis_connection("default").flushall()
        self.cache = get_redis_connection()
        self.execute_caches()
        return super().setUp()
