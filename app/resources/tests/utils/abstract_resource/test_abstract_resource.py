from unittest import TestCase
from unittest.mock import patch
from resources.utils.base_resource import BaseResource


class BaseResourceTestCase(TestCase):

    @patch("resources.utils.base_resource.BaseResource.__abstractmethods__", set())
    def test_abstract_methods_raise_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            BaseResource("https://dummmy/url/").fetch_all()
            BaseResource("https://dummmy/url/").get_cache_source()
