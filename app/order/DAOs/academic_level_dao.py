"""Fetches academic_levels and returns a list containing academic_level objects
"""
import json
from django_redis import get_redis_connection
from order.domain_objects.academic_level_object import AcademicLevelObject
from order.DAOs.data_from_file import DataFromFile


class AcademicLevelDAO():
    """Defines a list of Academic Levels.
    """

    def __init__(self) -> None:
        self.cache = DataFromFile()
        self.objects = []
        self.get_academic_levels()

    def get_academic_levels(self):
        cached_academic_levels = []
        if self.cache.get("academic_levels"):
            cached_academic_levels = json.loads(
                self.cache.get("academic_levels"))
        for academic_level in cached_academic_levels:
            academic_level_object = AcademicLevelObject(
                academic_level['academic_level_name'],
                academic_level['academic_level_display_name'],
                academic_level['base_price']
            )
            self.objects.append(academic_level_object)

    def __len__(self):
        return len(self.objects)

    def __iter__(self):
        for item in self.objects:
            yield item
