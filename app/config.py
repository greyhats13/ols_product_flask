# create config helper class to store all the config variables for flas_sqlalchemy mysql, redis, jwt, etc from environment variables

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # SQL Alchemy Config
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + os.environ.get('DB_USER') + ':' + os.environ.get('DB_PASSWORD') + '@' + os.environ.get('DB_HOST') + ':' + os.environ.get('DB_PORT') + '/' + os.environ.get('DB_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_RECORD_QUERIES = os.environ.get('SQLALCHEMY_RECORD_QUERIES')
    
    # redis URL from environment variable
    # CACHE_TYPE = os.environ['CACHE_TYPE']
    # CACHE_REDIS_HOST = os.environ['CACHE_REDIS_HOST']
    # CACHE_REDIS_PORT = os.environ['CACHE_REDIS_PORT']
    # CACHE_REDIS_DB = os.environ['CACHE_REDIS_DB']
    # CACHE_REDIS_URL = os.environ['CACHE_REDIS_URL']
    # CACHE_DEFAULT_TIMEOUT = os.environ['CACHE_DEFAULT_TIMEOUT']
    # create flask app config from environment variables
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    FLASK_RUN_HOST = os.environ.get('FLASK_RUN_HOST')
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')