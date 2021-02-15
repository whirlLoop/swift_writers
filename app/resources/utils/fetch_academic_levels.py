"""Fetch academic levels and set in cache
"""
import requests
from django.conf import settings
from resources.utils.base_resource import BaseResource


class FetchAcademicLevels(BaseResource):

    def __init__(self):
        super().__init__(settings.BASE_ACADEMIC_LEVELS_URL)

    def fetch_all(self):
        request = requests.get(self.base_url)
        results = request.text
        if not self.cache.exists('academic_levels'):
            self.cache.set('academic_levels', results)
