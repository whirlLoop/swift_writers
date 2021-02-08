import redis
from django.conf import settings

def connect_to_redis():
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


redis_connection = connect_to_redis()
