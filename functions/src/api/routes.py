from flask import Blueprint, Response, request
import json
from client.searchResultsProduct import searchProduct
from client.searchProductDetailsById import showProductDetails

api = Blueprint('api', __name__)

@api.route("/")
def root():
    return "Hello world - from Flask!"

@api.route("/products/<product_name>")
def findProducts(product_name):
    products = searchProduct(product_name)
    response = json.dumps(products, ensure_ascii=False, indent=2)
    return Response(response, mimetype='application/json; charset=utf-8')

@api.route("/products/item/<product_id>")
def productDetails(product_id):
    data = showProductDetails(product_id)
    jsonData = json.dumps(data, ensure_ascii=False, indent=2)
    return Response(jsonData, mimetype='application/json; charset=utf-8')

def register_routes(app):
    app.register_blueprint(api)
