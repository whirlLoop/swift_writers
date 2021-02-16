"""Fetches academic_levels and returns a list containing academic_level objects
"""
import json
from django_redis import get_redis_connection
from order.domain_objects.academic_level_object import AcademicLevelObject


class AcademicLevelDAO():

    def __init__(self) -> None:
        self.cache = get_redis_connection()

    def get_academic_levels(self):
        cached_academic_levels = json.loads(self.cache.get("academic_levels"))
        academic_level_objects = []
        for academic_level in cached_academic_levels:
            academic_level_object = AcademicLevelObject(
                academic_level['academic_level_display_name'],
                academic_level['base_price']
            )
            academic_level_objects.append(academic_level_object)
        return academic_level_objects
