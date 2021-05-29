from model.product import Product,ProductSchema
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy


class Service (object):
    def __init__(self,app:Flask,db:SQLAlchemy) -> None:
        self.app=app
        self.db=db
        self.product_schema = ProductSchema()
        self.products_schema=ProductSchema(many=True)

    def add_product(self):
        name=request.json['name']
        description=request.json['description']
        price=request.json['price']
        qty=request.json['qty']

        new_product = Product(name,description,price,qty)
        self.db.session.add(new_product)
        self.db.session.commit()
        return self.product_schema.jsonify(new_product)

    def get_products(self):
        all_products = Product.query.all()
        result = self.products_schema.dump(all_products)
        return jsonify(result)
    def get_product(self,id):
        product = Product.query.get(id)
        return self.product_schema.jsonify(product)
        # @app.route('/product/<id>',methods=['GET'])
# def get_product(id):
#     product = Product.query.get(id)
#     return product_schema.jsonify(product)