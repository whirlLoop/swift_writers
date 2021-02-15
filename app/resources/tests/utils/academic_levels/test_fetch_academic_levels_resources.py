import json
from resources.utils import FetchAcademicLevels
from resources.tests.common.base_test_case import BaseTestCase


class FetchAcademicLevelsTestCase(BaseTestCase):

    def setUp(self):
        super(FetchAcademicLevelsTestCase, self).setUp()
        self.fetch_instance = FetchAcademicLevels()

    def test_fetched_academic_levels_set_in_cache(self):
        self.cache.delete('academic_levels')
        self.fetch_instance.fetch_all()
        self.assertIsInstance(json.loads(
            self.cache.get("academic_levels")), list)
        self.assertIsInstance(json.loads(
            self.cache.get("academic_levels"))[0], dict)
