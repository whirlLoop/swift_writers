"""Fetches essays and returns a list containing essay objects
"""
import json
from order.domain_objects.essay_object import EssayObject
from order.DAOs.base_dao import BaseDAO


class EssayDAO(BaseDAO):
    """Returns a list of essay objects.
    """

    def __init__(self) -> None:
        super().__init__()
        self.get_essays()

    def get_essays(self):
        cached_essays = []
        if self.cache.get("essays"):
            cached_essays = json.loads(self.cache.get("essays"))
        for essay in cached_essays:
            essay_object = EssayObject(
                essay['essay_name'], essay['essay_display_name'],
                essay['price_per_page']
            )
            self.objects.append(essay_object)
