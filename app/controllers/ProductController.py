#create ProductController and ProductListController class from ProductModel class, flask_restful Resource class and flask_restful reqparse class, and import cache from ap
from app.models.ProductModel import ProductModel
from flask_restful import Resource, reqparse
# from app import cache
from flask_healthz import HealthError

# create ProductController class from flask_restful Resource class
class ProductController(Resource):
    # create ProductController class get method
    # @cache.cached(timeout=60)
    def get(self, id):
        product = ProductModel.get_by_id(id)
        if product:
            return product.serialize()
        return {'message': 'Product not found'}, 404
    # create ProductController class put method
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('sku', type=str, required=True)
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('price', type=float, required=True)
        parser.add_argument('quantity', type=int, required=True)
        parser.add_argument('category', type=str, required=True)
        parser.add_argument('weight', type=float, required=True)
        parser.add_argument('volume', type=float, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('image', type=str, required=True)
        data = parser.parse_args()
        product = ProductModel.update_by_id(id, data)
        if product:
            return product.serialize(), 201
        return {'message': 'Product not found'}, 404
    # create ProductController class delete method
    def delete(self, id):
        product = ProductModel.delete_by_id(id)
        if product:
            return product.serialize()
        return {'message': 'Product not found'}, 404

# create ProductListController class from flask_restful Resource class
class ProductListController(Resource):
    # create ProductListController class get method
    # @cache.cached(timeout=60)
    def get(self):
        products = ProductModel.get_all()
        if products:
            return [product.serialize() for product in products]
        return {'message': 'Products not found'}, 404
    # create ProductListController class post method
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sku', type=str, required=True)
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('price', type=float, required=True)
        parser.add_argument('quantity', type=int, required=True)
        parser.add_argument('category', type=str, required=True)
        parser.add_argument('weight', type=float, required=True)
        parser.add_argument('volume', type=float, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('image', type=str, required=True)
        data = parser.parse_args()
        product = ProductModel.create(data)
        if product:
            return product.serialize(), 201
        return {'message': 'Product not created'}, 500

class ProductHealthController():
    def liveness():
        try:
           ProductModel.check_mysql_connection()
        except Exception as e:
            raise HealthError(e)

    def readiness():
        try:
            ProductModel.check_mysql_connection()
        except Exception as e:
            raise HealthError(e)

