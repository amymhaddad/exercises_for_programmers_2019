"""Function retreives data from json file"""

import json


def access_json_data(file):
    """Read in data from json file and convert it to a Python dictionary"""
    with open(file) as inventory:
        return json.load(inventory)
