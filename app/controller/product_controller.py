from app import Product
from flask import Flask, request


class Product_Controller():
    def __init__(self,app:Flask) -> None:
        self.app=app

    @app.route('/product/',methods=['POST'])
    @app.route('/product',methods=['POST'])
    def add_product():
        name=request.json['name']
        description=request.json['description']
        price=request.json['price']
        qty=request.json['qty']

        new_product = Product(name,description,price,qty)
        return product_schema.jsonify(new_product)
