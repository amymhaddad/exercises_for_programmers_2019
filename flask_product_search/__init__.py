from flask import Flask 
app = Flask(__name__)

from flask_product_search import routes
# from flask_product_search import v2_extract_products