from datetime import datetime
from app.models.ProductModel import ProductModel
from flask_restful import Resource, reqparse
from app import redis
from flasgger import swag_from

class ProductController(Resource):
    # Retrieve a product by its ID, with caching
    @redis.cached(timeout=60)
    @swag_from('docs/product_get.yml')
    def get(self, id):
        product = ProductModel.get_by_id(id)
        if product:
            return product.serialize()
        return {'message': 'Product not found'}, 404

    # Update a product by its ID
    @swag_from('docs/product_put.yml')
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('sku', type=str, required=False)
        parser.add_argument('name', type=str, required=False)
        parser.add_argument('price', type=float, required=False)
        parser.add_argument('quantity', type=int, required=False)
        parser.add_argument('category', type=str, required=False)
        parser.add_argument('weight', type=float, required=False)
        parser.add_argument('volume', type=float, required=False)
        parser.add_argument('description', type=str, required=False)
        parser.add_argument('image', type=str, required=False)
        data = parser.parse_args()

        data = {k: v for k, v in data.items() if v is not None}

        product = ProductModel.update_by_id(id, data)
        if product:
            return product.serialize(), 201
        return {'message': 'Product not found'}, 404

    # Delete a product by its ID
    @swag_from('docs/product_delete.yml')
    def delete(self, id):
        product = ProductModel.delete_by_id(id)
        if product:
            return product.serialize()
        return {'message': 'Product not found'}, 404

class ProductListController(Resource):
    # Retrieve all products, with caching
    @redis.cached(timeout=60)
    @swag_from('docs/products_get.yml')
    def get(self):
        products = ProductModel.get_all()
        if products:
            return [product.serialize() for product in products]
        return {'message': 'Products not found'}, 404
    
    # Create a new product
    @swag_from('docs/products_post.yml')
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
        data["date_created"] = datetime.utcnow()
        product = ProductModel.create(data)
        if product:
            return product.serialize(), 201
        return {'message': 'Product not created'}, 500