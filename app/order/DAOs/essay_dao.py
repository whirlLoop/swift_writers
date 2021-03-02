"""Fetches essays and returns a list containing essay objects
"""
import json
from django_redis import get_redis_connection
from order.domain_objects.essay_object import EssayObject


class EssayDAO():
    """Returns a list of essay objects.
    """

    def __init__(self) -> None:
        self.cache = get_redis_connection()
        self.objects = []
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

    def __len__(self):
        return len(self.objects)

    def __iter__(self):
        for item in self.objects:
            yield item
