
from flask_sqlalchemy import SQLAlchemy
from ..model.product import Product,ProductSchema

def addProduct(product:Product,db:SQLAlchemy):
    db.session.add(product)
    db.session.commit()
    return product