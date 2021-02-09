"""Fetch essays and set in cache
"""
import requests
from django.conf import settings
from django_redis import get_redis_connection


class FetchEssays():

    def __init__(self):
        self.cache = get_redis_connection()
        self.base_url = settings.BASE_ESSAYS_URL

    def fetch_all(self):
        request = requests.get(self.base_url)
        results = request.text
        if not self.cache.exists('key'):
            self.cache.set('essays', results)
