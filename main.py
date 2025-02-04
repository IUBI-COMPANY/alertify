from flask import Flask, Response
import json
from clientScraper.searchResultsProduct import searchProduct

app = Flask(__name__)

@app.route("/")
def root():
    return "Home"

@app.route("/products/<product_name>")
def findProducts(product_name):
    products = searchProduct(product_name)
    response = json.dumps(products, ensure_ascii=False, indent=2)
    return Response(response, mimetype='application/json; charset=utf-8')

@app.route("/products/item/<product_id>")
def productDetails(product_id):
    return product_id



if __name__ == '__main__':
    app.run(debug=True)
