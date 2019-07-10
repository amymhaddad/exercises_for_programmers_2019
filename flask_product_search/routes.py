from flask_product_search import app
import json
from flask import render_template


def convert_json_data(file):
    """Read in the data from a json file and convert it to a Python object"""
    with open(file, mode="r") as json_object:
        data = json_object.read()
        return json.loads(data)


def show_all_products(products):
    """Return all products"""

    all_products = {}
    for product in products:
        all_products[product["name"]] = product
    return all_products


def one_product(products, itemname):
    """Return a single product based on user input"""
    for product in products:
        if product["name"] == itemname:
            return product


@app.route("/")
def products():
    products_json = convert_json_data("products.json")
    products = products_json["products"]
    all_products = show_all_products(products)

    return render_template("products.html", title="Product", all_products=all_products)


@app.route("/product/<itemname>")
def single_product(itemname):
    products_json = convert_json_data("products.json")
    products = products_json["products"]
    single_product = one_product(products, itemname)

    return render_template("single_product.html", title="Product", products=products, single_product=single_product)


if __name__ == "__main__":
    app.run()
