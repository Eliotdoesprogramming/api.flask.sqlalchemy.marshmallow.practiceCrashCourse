from marshmallow.fields import Number
from service.apiservice import Service
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from model.product import Product,ProductSchema
class ProductController(object):
    def __init__(self,app:Flask,db:SQLAlchemy,service:Service):
        self.app=app
        self.db=db
        self.product_schema = ProductSchema()
        self.products_schema = ProductSchema(many=True)
        self.service=service
        self.add_routes(app)


    def add_routes(self,app:Flask)->None:
        app.add_url_rule('/product',methods=['GET'],view_func=self.get_all_products)
        app.add_url_rule('/product',methods=['POST'],view_func=self.add_product)
        app.add_url_rule('/product/<id>',methods=['GET'],view_func=self.get_product)
    def get_all_products(self):
        return self.service.get_products()
    
    def add_product(self):
        return self.service.add_product()
    def get_product(self,id:Number):
        return self.service.get_product(id)


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