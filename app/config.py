import os

# Get the absolute path of the parent directory
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # SQL Alchemy Config
    # Construct the database URI from environment variables
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + os.environ.get('DB_USER') + ':' + os.environ.get('DB_PASSWORD') + '@' + os.environ.get('DB_HOST') + ':' + os.environ.get('DB_PORT') + '/' + os.environ.get('DB_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_RECORD_QUERIES = os.environ.get('SQLALCHEMY_RECORD_QUERIES')
    
    # Redis Config
    # Get the Redis configuration from environment variables
    CACHE_TYPE = os.environ['CACHE_TYPE']
    CACHE_REDIS_HOST = os.environ['CACHE_REDIS_HOST']
    CACHE_REDIS_PORT = os.environ['CACHE_REDIS_PORT']
    CACHE_REDIS_DB = os.environ['CACHE_REDIS_DB']
    CACHE_REDIS_PASSWORD = os.environ['CACHE_REDIS_PASSWORD']
    CACHE_DEFAULT_TIMEOUT = os.environ['CACHE_DEFAULT_TIMEOUT']
    
    # Flask Config
    # Get the Flask configuration from environment variables
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    FLASK_RUN_HOST = os.environ.get('FLASK_RUN_HOST')
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')

    # Health Check Config
    HEALTHZ = {
        "liveness": "app.healthz.live",
        "readiness": "app.healthz.ready",
    }