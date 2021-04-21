"""Fetches academic_levels and returns a list containing academic_level objects
"""
import json
from order.domain_objects.academic_level_object import AcademicLevelObject
from order.DAOs.base_dao import BaseDAO


class AcademicLevelDAO(BaseDAO):
    """Defines a list of Academic Levels.
    """

    def __init__(self) -> None:
        super().__init__()
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
