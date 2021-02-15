"""Fetch academic levels and set in cache
"""
import requests
from django.conf import settings
from django_redis import get_redis_connection


class FetchAcademicLevels():

    def __init__(self):
        self.cache = get_redis_connection()
        self.base_url = settings.BASE_ACADEMIC_LEVELS_URL

    def fetch_all(self):
        request = requests.get(self.base_url)
        results = request.text
        if not self.cache.exists('academic_levels'):
            self.cache.set('academic_levels', results)
