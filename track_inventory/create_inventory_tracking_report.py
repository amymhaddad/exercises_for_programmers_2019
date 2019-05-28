"""Get user input and create an inventory report"""


from prettytable import from_csv
from inventory_report import InventoryReport


def get_inventory_report_name():
    """Get user's inventory report name"""
    print("Enter information about your personal invenvtory when prompted.")
    print("Type 'q' to quit.\n")

    report_name = input("Enter the type of inventory report you'd like to create: ")
    return InventoryReport(report_name)


def get_inventory_report_details():
    """Compile inventory details from user and store details into a dictionary"""
    report = get_inventory_report_name()

    while True:
        item = input("Enter an item: ")

        if item == "q":
            break

        serial_number = input("Enter a serial number: ")
        value = input("Enter a value: ")

        try:
            float_value = float(value)
        except:
            print("You must enter a numeric value.")
            value = input("Enter a value: ")
        else:
            value = f"{float_value:.2f}"

        report.add_detail_to_report(item, serial_number, value)
        print("\n")

    return report


def remove_report_item(report):
    """Remove an item from the inventory report"""
    item_to_remove = input("Provide the serial number for the item you want removed: ")
    return report.remove_item_from_report(item_to_remove)


def csv_tablular_report(filename):
    """Compile inventory report and generate a tablular report"""
    csv_file = open(filename)
    return from_csv(csv_file)
