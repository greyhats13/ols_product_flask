#create mysql helper class using flask_sqlalchemy

from flask_sqlalchemy import SQLAlchemy

class MySQLHelper:
    def __init__(self, app):
        self.db = SQLAlchemy(app)

    def get_all(self, model):
        return model.query.all()
    
    def get_by_id(self, model, id):
        return model.query.get(id)
    
    def update_by_id(self, model, id, data):
        model.query.filter_by(id=id).update(data)
        self.db.session.commit()
        return model.query.get(id)
    
    def delete_by_id(self, model, id):
        model.query.filter_by(id=id).delete()
        self.db.session.commit()
        return True
    
    def create(self, model, data):
        new_model = model(**data)
        self.db.session.add(new_model)
        self.db.session.commit()
        return new_model
    
    def create_all(self):
        self.db.create_all()

    def execute_one(self):
        return self.db.engine.execute("SELECT 1")