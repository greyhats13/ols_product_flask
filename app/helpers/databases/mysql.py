from flask_sqlalchemy import SQLAlchemy

class MySQLHelper:
    def __init__(self, app):
        self.db = SQLAlchemy(app)

    # Get all records from a model
    def get_all(self, model):
        return model.query.all()
    
    # Get a record by its ID from a model
    def get_by_id(self, model, id):
        return model.query.get(id)
    
    # Update a record by its ID with the given data
    def update_by_id(self, model, id, data):
        model.query.filter_by(id=id).update(data)
        self.db.session.commit()
        return model.query.get(id)
    
    # Delete a record by its ID
    def delete_by_id(self, model, id):
        model.query.filter_by(id=id).delete()
        self.db.session.commit()
        return True
    
    # Create a new record with the given data
    def create(self, model, data):
        new_model = model(**data)
        self.db.session.add(new_model)
        self.db.session.commit()
        return new_model
    
    # Create all tables
    def create_all(self):
        self.db.create_all()

    # Check the connection to the MySQL database
    def check_connection(self):
        return self.db.engine.connect()
