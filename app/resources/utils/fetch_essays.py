"""Fetch essays and set in cache
"""
import requests
from django.conf import settings
from resources.utils.base_resource import BaseResource


class FetchEssays(BaseResource):

    def __init__(self):
        super().__init__(settings.BASE_ESSAYS_URL)

    def fetch_all(self):
        request = requests.get(self.base_url)
        results = request.text
        if not self.cache.exists('essays'):
            self.cache.set('essays', results)
