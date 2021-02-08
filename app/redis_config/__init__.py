import redis
from django.conf import settings


def get_redis_connection():
    """Connects to redis server

    Returns:
        object: redis connection
    """
    conn = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB
    )
    return conn
