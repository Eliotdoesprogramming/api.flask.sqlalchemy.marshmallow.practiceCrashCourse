from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


#Product class/model
class Product(SQLAlchemy.Model):
    id = SQLAlchemy.Column(SQLAlchemy.Integer, primary_key=True)
    name = SQLAlchemy.Column(SQLAlchemy.String(100), unique=True)
    description = SQLAlchemy.Column(SQLAlchemy.String(200))
    price = SQLAlchemy.Column(SQLAlchemy.Float)
    qty = SQLAlchemy.Column(SQLAlchemy.Integer)

    def __init__(self,name,description,price,qty) -> None:
        self.name=name
        self.description=description
        self.price=price
        self.qty=qty


#Product ScheMarshmallow
class ProductSchema(Marshmallow.Schema):
    class Meta:
        fields = ('id','name','description','price','qty')