# create routes from ProductController and ProductListController classes
from app import app, api
from app.controllers.ProductController import ProductController, ProductListController, ProductHealthController
from flask_healthz import healthz, HealthError

# Product endpoints
api.add_resource(ProductController, '/product/<int:id>')
api.add_resource(ProductListController, '/products')

# Healthcheck endpoints
app.register_blueprint(healthz, url_prefix="/healthz")
app.config.update(
    HEALTHZ = {
        "live": ProductHealthController.liveness,
        "ready": ProductHealthController.readiness,
    }
)