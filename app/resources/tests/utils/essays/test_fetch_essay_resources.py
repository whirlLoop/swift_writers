import json
from resources.utils import FetchEssays
from resources.utils.base_resource import BaseResource
from resources.tests.common.base_test_case import BaseTestCase
import pytest


class FetchEssaysTestCase(BaseTestCase):

    def setUp(self):
        super(FetchEssaysTestCase, self).setUp()
        self.fetch_instance = FetchEssays()

    def test_fetched_essays_set_in_cache(self):
        with pytest.raises(Exception):
            self.cache.delete('essays')
            self.fetch_instance.fetch_all()
            self.assertIsInstance(json.loads(
                self.fetch_instance.cache.get("essays")), list)
            self.assertIsInstance(json.loads(
                self.fetch_instance.cache.get("essays"))[0], dict)

    def test_implements_base_resource_abastract_class(self):
        self.assertIsInstance(self.fetch_instance, BaseResource)

    def test_essays_set_even_if_api_inaccessible(self):
        with pytest.raises(Exception):
            self.fetch_instance.base_url = (
                'https://writing-service-backend-production-ge4s7xbpfq-ue.a.run.app/v1/essays/nothing/'
            )
            self.cache.delete('essays')
            self.fetch_instance.fetch_all()
            self.assertIsInstance(json.loads(
                self.fetch_instance.cache.get("essays")), list)

    def test_raise_request_exceptions(self):
        self.cache.delete('essays')
        with self.assertRaises(Exception):
            self.fetch_instance.base_url = (
                'https://writing-service-backend-production-ge4s7xbpfq-ue.a.run.app/v1/essays/nothing/'
            )
            self.fetch_instance.fetch_all()
