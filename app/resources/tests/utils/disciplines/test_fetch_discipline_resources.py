import json
from resources.utils import FetchDisciplines
from resources.utils.base_resource import BaseResource
from resources.tests.common.base_test_case import BaseTestCase
import pytest


class FetchDisciplinesTestCase(BaseTestCase):

    def setUp(self):
        super(FetchDisciplinesTestCase, self).setUp()
        self.fetch_instance = FetchDisciplines()

    def test_fetched_discipline_set_in_cache(self):
        with pytest.raises(Exception):
            self.cache.delete('Discipline')
            self.fetch_instance.fetch_all()
            self.assertIsInstance(json.loads(
                self.fetch_instance.cache.get("discipline")), list)
            self.assertIsInstance(json.loads(
                self.fetch_instance.cache.get("discipline"))[0], dict)

    def test_implements_base_resource_abastract_class(self):
        self.assertIsInstance(self.fetch_instance, BaseResource)

    def test_discipline_set_even_if_api_inaccessible(self):
        with pytest.raises(Exception):
            self.fetch_instance.base_url = (
                'https://writing-service-backend-production-ge4s7xbpfq-ue.a.run.app/v1/discipline/nothing/'
            )
            self.cache.delete('Discipline')
            self.fetch_instance.fetch_all()
            self.assertIsInstance(json.loads(
                self.fetch_instance.cache.get("discipline")), list)

    def test_raise_request_exceptions(self):
        self.cache.delete('Discipline')
        with self.assertRaises(Exception):
            self.fetch_instance.base_url = (
                'https://writing-service-backend-production-ge4s7xbpfq-ue.a.run.app/v1/discipline/nothing/'
            )
            self.fetch_instance.fetch_all()
