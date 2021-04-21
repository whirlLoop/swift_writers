"""Fetch essays and set in cache
"""
import requests
from django.conf import settings
from resources.utils.base_resource import BaseResource
from order.DAOs.data_from_file import DataFromFile


class FetchDisciplines(BaseResource):

    def __init__(self):
        super().__init__(settings.BASE_DISCIPLINES_URL)

    def fetch_all(self):
        try:
            request = requests.get(self.base_url, timeout=5)
            request.raise_for_status()
            results = request.text
            if not self.cache.exists('disciplines'):
                self.cache.set('disciplines', results)
        except requests.exceptions.RequestException as exception:
            self.cache.set('disciplines', DataFromFile().essays)
            # log exception
            raise exception

    def get_cache_source(self, cache_source):
        return cache_source
