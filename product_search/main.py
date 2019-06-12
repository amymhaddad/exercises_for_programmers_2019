"""Return the inventory details for an item in the product inventory"""

import sys
from product_search import (
    validate_item,
    inventory_details_for_user_item,
    _style_dictionary_items_for_output,
    return_product_details,
)
from data_management import access_json_data

from user_input import get_item_name_from_user


def main(filename):
    """
    Calls to functions to get valid user input, 
    retrieve inventory details based on input, 
    and return details to user
    """
    # input
    data = access_json_data(sys.argv[1])
    item = get_valid_item_input(data)

    # core
    inventory = inventory_details_for_user_item(item, data)
    inventory_for_output = _style_dictionary_items_for_output(inventory)

    # output
    output_for_user = return_product_details(inventory_for_output)
    print(output_for_user)


def get_valid_item_input(data):
    """Prompt user until recieve valid item name"""

    while True:
        #take this line out b/c I'm redoing work. 
        # data = access_json_data(sys.argv[1])
        item_to_search = get_item_name_from_user()
        product_in_inventory = validate_item(item_to_search, data)

        if product_in_inventory == True:
            return item_to_search
        else:
            print("Sorry, that product was not found in our inventory.")


if __name__ == "__main__":
    try:
        main(sys.argv[1])

    except IndexError:
        print("This file is not found.")
