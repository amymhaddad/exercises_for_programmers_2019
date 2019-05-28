"""Create and return an inventory tracking report"""

import sys
from inventory_tracking_management import write_inventory_to_csv

from create_inventory_tracking_report import (
    get_inventory_report_details,
    csv_tablular_report,
)


def main(filename):
    """Get user input for inventory items and print a tabular report"""
    inventory = get_inventory_report_details()

    write_inventory_to_csv(filename, inventory)

    generate_tabular_report = csv_tablular_report(filename)
    print(generate_tabular_report)


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        print("This file is not found.")
