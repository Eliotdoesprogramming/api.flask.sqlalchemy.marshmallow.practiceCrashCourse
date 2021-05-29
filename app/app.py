from service.apiservice import Service
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# from .models.product import Product, ProductSchema



#Init app
app=Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))





#db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#initdb
#sqlalchemy https://docs.sqlalchemy.org/en/14/



#init ma
#https://marshmallow-sqlalchemy.readthedocs.io/en/latest/
db = SQLAlchemy(app)
ma = Marshmallow(app)
from controller.prodcontroller import ProductController
from model.product import Product,ProductSchema
service = Service(app,db)
pc = ProductController(app,db,service)



#region
# #Product class/model
# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True)
#     description = db.Column(db.String(200))
#     price = db.Column(db.Float)
#     qty = db.Column(db.Integer)

#     def __init__(self,name,description,price,qty) -> None:
#         self.name=name
#         self.description=description
#         self.price=price
#         self.qty=qty


# #Product Schema
# class ProductSchema(ma.Schema):
#     class Meta:
#         fields = ('id','name','description','price','qty')

# class Purchase(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     product_id = db.Column(db.ForeignKey('product.id'))

#     def __init__(self,name,product_id) -> None:
#         self.name=name
#         self.product_id=product_id


# # Purchase Schema
# class PurchaseSchema(ma.Schema):
#     class Meta(ma.Schema):
#         fields = ('id','name','product_id')

#Init schema

# product_schema = ProductSchema()
# products_schema = ProductSchema(many=True)

# purchase_schema = PurchaseSchema()
# purchases_schema = PurchaseSchema(many=True)




#Routes
# @app.route('/product/',methods=['POST'])
# @app.route('/product',methods=['POST'])
# def add_product():
#     name=request.json['name']
#     description=request.json['description']
#     price=request.json['price']
#     qty=request.json['qty']

#     new_product = Product(name,description,price,qty)
#     db.session.add(new_product)
#     db.session.commit()
#     return product_schema.jsonify(new_product)


# @app.route('/product/',methods=['GET'])
# @app.route('/product',methods=['GET'])
# def get_all_products():
#     all_products = Product.query.all()
#     result = products_schema.dump(all_products)
#     return jsonify(result)


# @app.route('/product/<id>',methods=['GET'])
# def get_product(id):
#     product = Product.query.get(id)
#     return product_schema.jsonify(product)

# @app.route('/product/<id>',methods=['PUT'])
# def update_product(id):
#     product = Product.query.get(id)
#     product.name=request.json['name']
#     product.description=request.json['description']
#     product.price=request.json['price']
#     product.qty=request.json['qty']


#     db.session.commit()
#     return product_schema.jsonify(product)


# @app.route('/product/<id>',methods=['DELETE'])
# def delete_product(id):
#     product = Product.query.get(id)
#     db.session.delete(product)
#     db.session.commit()
#     return product_schema.jsonify(product)

#endregion

#Run Server
if(__name__== '__main__'):
    app.run(debug=True)


