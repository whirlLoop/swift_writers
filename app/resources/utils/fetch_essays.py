"""Fetch essays and set in cache
"""
import requests
from django.conf import settings
from resources.utils.base_resource import BaseResource
from order.DAOs.data_from_file import DataFromFile


class FetchEssays(BaseResource):

    def __init__(self):
        super().__init__(settings.BASE_ESSAYS_URL)

    def fetch_all(self):
        try:
            request = requests.get(self.base_url, timeout=5)
            request.raise_for_status()
            results = request.text
            if not self.cache.exists('essays'):
                self.cache.set('essays', results)
        except requests.exceptions.RequestException as exception:
            self.cache.set('essays', DataFromFile().essays)
            # log exception
            raise exception

    def get_cache_source(self, cache_source):
        return cache_source
