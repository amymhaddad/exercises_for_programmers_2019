"""Practice file that returns inventory details that I use in templates"""

import json


def convert_json_data(file):
    """Read in the data from a json file and convert it to a Python object"""
    with open(file, mode="r") as json_object:
        data = json_object.read()
        return json.loads(data)


products_json = convert_json_data("products.json")
products = products_json["products"]


def show_all_products(products):
    all_products = {}
    for product in products:
        all_products[product["name"]] = product

    return all_products


inventory = show_all_products(products)

for name, details in inventory.items():
    for category, detail in details.items():
        print(category, detail)


def show_all_products(products):
    """Display all provects from json file"""

    display_product = ""
    for product in products:
        for category, detail in product.items():
            if category == "price":
                detail = f"${product['price']:.2f}"
            display_product += f"{category.title()}: {detail}" + "\n"
    return display_product


def one_product(products, itemname):
    """Return a single product based on user input"""

    inventory_details = ""

    for product in products:
        if product["name"] == itemname:
            for category, detail in product.items():
                if category == "price":
                    detail = f"${product['price']:.2f}"
                inventory_details += f"{category.title()}: {detail}" + "\n"
    return inventory_details


print(one_product(products, "Thing"))


# for products in products_json['products']:
#     for category, details in products.items():
#         print(category, details)
