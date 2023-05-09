from app import api
from app.controllers.ProductController import ProductController, ProductListController

# Add resources to the API
api.add_resource(ProductController, '/product/<int:id>')
api.add_resource(ProductListController, '/products')
