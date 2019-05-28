"""Template to store inventory report data """
from inventory_item import InventoryItem


class InventoryReport:
    def __init__(self, inventory_report_name):
        self.inventory_report_name = inventory_report_name
        self.inventory_tracker = {}

    def add_detail_to_report(self, item, serial_number, value):
        """Create an inventory report"""

        inventory_details = InventoryItem(item, serial_number, value)
        self.inventory_tracker[serial_number] = inventory_details
        return inventory_details

    def remove_item_from_report(self, serial_number):
        """Remove an item from an inventory"""
        del self.inventory_tracker[serial_number]

    def __repr__(self):
        """Return the inventory report name and the information associated with it"""
        return f"{self.inventory_report_name} {self.inventory_tracker}"
