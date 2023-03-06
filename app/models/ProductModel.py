# create product model from flask_sqlalchemy

from app import mysql

class ProductModel(mysql.db.db.Model):
    __tablename__ = 'products'
    id = mysql.db.Column(mysql.db.Integer, primary_key=True)
    sku = mysql.db.Column(mysql.db.String(100), unique=True)
    name = mysql.db.Column(mysql.db.String(50), nullable=False)
    price = mysql.db.Column(mysql.db.Float, nullable=False)
    quantity = mysql.db.Column(mysql.db.Integer, nullable=False)
    category = mysql.db.Column(mysql.db.String(50), nullable=False)
    weight = mysql.db.Column(mysql.db.Float, nullable=False)
    volume = mysql.db.Column(mysql.db.Float, nullable=False)
    description = mysql.db.Column(mysql.db.String(200), nullable=False)
    image = mysql.db.Column(mysql.db.String(200), nullable=False)
    date_created = mysql.db.Column(mysql.db.DateTime, nullable=False)
    
    #create product model init method
    def __init__(self, sku, name, price, quantity, category, weight, volume, description, image, date_created):
        self.sku = sku
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.weight = weight
        self.volume = volume
        self.description = description
        self.image = image
        self.date_created = date_created
        
    def __repr__(self):
        return '<Product %r>' % self.name
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'category': self.category,
            'description': self.description,
            'image': self.image,
            'date_created': str(self.date_created)
        }
        
    # create product model getters and setters using mysql.db helper class
    def get_all():
        return mysql.get_all(ProductModel)
    
    def get_by_id(id):
        return mysql.get_by_id(ProductModel, id)
    
    def update_by_id(id, data):
        return mysql.update_by_id(ProductModel, id, data)
    
    def delete_by_id(id):
        return mysql.delete_by_id(ProductModel, id)
    
    def create(data):
        return mysql.create(ProductModel, data)
    
    def create_all():
        return mysql.create_all()
    
    def get_by_name(name):
        return mysql.get_by_name(ProductModel, name)
    
    def get_by_category(category):
        return mysql.get_by_category(ProductModel, category)
    
    def get_by_price(price):
        return mysql.get_by_price(ProductModel, price)
    
    def get_by_quantity(quantity):
        return mysql.get_by_quantity(ProductModel, quantity)
    
    def get_by_date_created(date_created):
        return mysql.get_by_date_created(ProductModel, date_created)
    
    def migrate_all():
        return mysql.migrate_all()

    # check DB connection
    def check_mysql_connection():
        return mysql.execute_one()
