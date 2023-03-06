# # create redis helper class from flask_caching

# from flask_caching import Cache
# from app.config import Config

# class RedisHelper:
#     def __init__(self, app):
#         self.cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_HOST': Config.CACHE_REDIS_HOST, 'CACHE_REDIS_PORT': Config.CACHE_REDIS_PORT, 'CACHE_REDIS_DB': Config.CACHE_REDIS_DB, 'CACHE_REDIS_PASSWORD': Config.CACHE_REDIS_PASSWORD})

#     def get(self, key):
#         return self.cache.get(key)

#     def set(self, key, value):
#         self.cache.set(key, value)

#     def delete(self, key):
#         self.cache.delete(key)

#     def clear(self):
#         self.cache.clear()