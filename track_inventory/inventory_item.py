"""Template to create an inventory report"""


class InventoryItem:
    def __init__(self, item, serial_number, value):
        self.item = item
        self.serial_number = serial_number
        self.value = value

    def __repr__(self):
        """Return inventory information"""
        return f"{self.item} {self.serial_number} {self.value}"
