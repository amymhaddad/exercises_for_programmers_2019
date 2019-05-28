"""Write report inventory to a json or csv file"""
import json
import csv


def write_inventory_to_json(filename, report):
    """Write user's inventory report to json file"""

    inventory_details = [
        str(report_details) for report_details in report.inventory_tracker.values()
    ]

    inventory = {
        "report type": report.inventory_report_name,
        "inventory": inventory_details,
    }

    with open(filename, mode="w") as file:
        json.dump(inventory, file)


def write_inventory_to_csv(filename, inventory):
    """Write user's inventory report to csv file"""
    with open(filename, mode="w", newline="") as csvfile:
        fieldnames = ["item", "serial number", "value"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for data in inventory.inventory_tracker.values():
            item = data.item
            serial_number = data.serial_number
            value = float(data.value)
            rounded_value = f"${value:.2f}"

            writer.writerow(
                {"item": item, "serial number": serial_number, "value": rounded_value}
            )
