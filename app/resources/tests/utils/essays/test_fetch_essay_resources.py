import json
from resources.utils import FetchEssays
from resources.tests.common.base_test_case import BaseTestCase


class FetchEssaysTestCase(BaseTestCase):

    def setUp(self):
        super(FetchEssaysTestCase, self).setUp()
        self.fetch_instance = FetchEssays()

    def test_fetched_essays_set_in_cache(self):
        self.cache.delete('essays')
        self.fetch_instance.fetch_all()
        self.assertIsInstance(json.loads(self.cache.get("essays")), list)
        self.assertIsInstance(json.loads(self.cache.get("essays"))[0], dict)
