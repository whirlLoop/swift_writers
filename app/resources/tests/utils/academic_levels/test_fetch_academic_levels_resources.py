import json
from resources.utils import FetchAcademicLevels
from resources.tests.common.base_test_case import BaseTestCase
from resources.utils.base_resource import BaseResource
import pytest


class FetchAcademicLevelsTestCase(BaseTestCase):

    def setUp(self):
        super(FetchAcademicLevelsTestCase, self).setUp()
        self.fetch_instance = FetchAcademicLevels()

    def test_fetched_academic_levels_set_in_cache(self):
        with pytest.raises(Exception):
            self.cache.delete('academic_levels')
            self.fetch_instance.fetch_all()
            self.assertIsInstance(json.loads(
                self.cache.get("academic_levels")), list)
            self.assertIsInstance(json.loads(
                self.cache.get("academic_levels"))[0], dict)

    def test_implements_base_resource_abastract_class(self):
        self.assertIsInstance(self.fetch_instance, BaseResource)

    def test_essays_set_even_if_api_inaccessible(self):
        with pytest.raises(Exception):
            self.fetch_instance.base_url = (
                'https://writing-service-backend-production-ge4s7xbpfq-ue.a.run.app/v1/academic_levels/nothing/'
            )
            self.cache.delete('academic_levels')
            self.fetch_instance.fetch_all()
            self.assertIsInstance(json.loads(
                self.fetch_instance.cache.get("academic_levels")), list)

    def test_raise_request_exceptions(self):
        self.cache.delete('academic_levels')
        with self.assertRaises(Exception):
            self.fetch_instance.base_url = (
                'https://writing-service-backend-production-ge4s7xbpfq-ue.a.run.app/v1/academic_levels/nothing/'
            )
            self.fetch_instance.fetch_all()
