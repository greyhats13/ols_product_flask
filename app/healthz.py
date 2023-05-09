from app import mysql, redis
from flask_healthz import HealthError

# Liveness check function
def live():
    try:
        mysql.check_connection()
        redis.get('healthcheck')
    except Exception as e:
        raise HealthError(f"Error: {e}")

# Readiness check function
def ready():
    try:
        mysql.check_connection()
        redis.get('healthcheck')
    except Exception as e:
        raise HealthError(f"Error: {e}")
