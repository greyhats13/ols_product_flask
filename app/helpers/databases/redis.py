from flask_caching import Cache
from app.config import Config

class RedisHelper:
    def __init__(self, app):
        self.cache = Cache(app, config={
            'CACHE_TYPE': app.config['CACHE_TYPE'],
            'CACHE_REDIS_HOST': app.config['CACHE_REDIS_HOST'],
            'CACHE_REDIS_PORT': app.config['CACHE_REDIS_PORT'],
            'CACHE_REDIS_DB': app.config['CACHE_REDIS_DB'],
            'CACHE_REDIS_PASSWORD': app.config['CACHE_REDIS_PASSWORD'],
            'CACHE_DEFAULT_TIMEOUT': app.config['CACHE_DEFAULT_TIMEOUT']
        })
    
    # Return the cache instance
    def get_cache(self):
        return self.cache
