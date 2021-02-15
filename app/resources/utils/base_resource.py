"""Contains a base class that abstracts common resource implementaion behavior.
"""
from abc import ABC, abstractmethod
from django_redis import get_redis_connection


class BaseResource(ABC):
    def __init__(self, base_url) -> None:
        self.cache = get_redis_connection()
        self.base_url = base_url
        super().__init__()

    @abstractmethod
    def fetch_all(self):
        pass
