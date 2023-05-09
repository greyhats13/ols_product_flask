from flask import Flask
from app.config import Config
from app.helpers.databases.mysql import MySQLHelper
from flask_migrate import Migrate
from app.helpers.databases.redis import RedisHelper
from flask_restful import Api
from flask_healthz import healthz

app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQLHelper(app)
mysql_migrate = Migrate(app, mysql.db)
redis = RedisHelper(app).get_cache()
api = Api(app)

app.register_blueprint(healthz)

from app import routes