"""Program that returns inventory details based for an inventory item"""


def validate_item(item_to_search, data):
    """Verify that the product exists: return True if it exists; return False if it doesn't"""

    for item in data["products"]:
        if item["name"] == item_to_search:
            return True
    return False


def inventory_details_for_user_item(item, data):
    """Return the dictionary associated with a specific user item"""

    for item_details in data["products"]:
        if item_details["name"] == item:
            return item_details


def style_dictionary_items_for_output(inventory):
    """Update keys, values in inventory dictionary for user readability"""
    user_inventory_items = {}

    for category, details in inventory.items():
        if category == "quantity":
            category = "Quantity on hand"
        if category == "price":
            details = "${0:.2f}".format(inventory["price"])
        user_inventory_items[category] = details
    return user_inventory_items


def return_product_details(inventory_for_output):
    """Return the product information associated with an item"""

    report_details = ""
    for category, details in inventory_for_output.items():
        report_details += f"{category.capitalize()}: {details}\n"
    return report_details.strip()
