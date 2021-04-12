"""Fetch academic levels and set in cache
"""
import requests
from django.conf import settings
from resources.utils.base_resource import BaseResource
from order.DAOs.data_from_file import DataFromFile


class FetchAcademicLevels(BaseResource):

    def __init__(self):
        super().__init__(settings.BASE_ACADEMIC_LEVELS_URL)

    def fetch_all(self):
        try:
            request = requests.get(self.base_url, timeout=5)
            request.raise_for_status()
            results = request.text
            if not self.cache.exists('academic_levels'):
                self.cache.set('academic_levels', results)
        except requests.exceptions.RequestException as exception:
            self.cache.set('academic_levels', DataFromFile().academic_levels)
            # log error
            raise exception
