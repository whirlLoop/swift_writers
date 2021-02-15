"""Fetches essays and returns a list containing essay objects
"""
import json
from django_redis import get_redis_connection
from order.domain_objects.essay_object import EssayObject


class EssayDAO():

    def __init__(self) -> None:
        self.cache = get_redis_connection()

    def get_essays(self):
        cached_essays = json.loads(self.cache.get("essays"))
        essay_objects = []
        for essay in cached_essays:
            essay_object = EssayObject(
                essay['essay_name'], essay['price_per_page']
            )
            essay_objects.append(essay_object)
        return essay_objects
