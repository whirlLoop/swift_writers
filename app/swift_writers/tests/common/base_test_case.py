from common.tests.base_test import BaseTestCase


class SwiftWritersBaseTestCase(BaseTestCase):

    def setUp(self) -> None:
        super(SwiftWritersBaseTestCase, self).setUp()
        self.execute_caches()
        return super().setUp()
