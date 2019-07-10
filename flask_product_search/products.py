import json

#convert json file into python object
def convert_json_data(file):
    """Read in the data from a json file and convert it to a Python object"""
    with open (file, mode='r') as json_object:
        data = json_object.read()
        return json.loads(data)

#set json data that's now a python object to projects_json
products_json = convert_json_data('products.json')

#Use the 'products' key from the products_json dictionary to get a LIST of dictionaries 
products = products_json['products']


def show_all_products(products):
    """Display all provects from json file"""

    display_product = ''
    #cycle through the list of dictionaries
    for product in products:
        #cycle through the dicionaries
        for category, detail in product.items():    
            if category == "price":
                detail = f"${product['price']:.2f}"
            display_product += f"{category.title()}: {detail}" + "\n"
    return display_product


def one_product(products, itemname):
    """Return a single product based on user input"""

    inventory_details = ''

    for product in products:
        if product['name'] == itemname:
            for category, detail in product.items():
                if category == 'price':
                    detail = f"${product['price']:.2f}"
                inventory_details += f"{category.title()}: {detail}" + "\n"
    return inventory_details

print(one_product(products, 'Thing'))
    