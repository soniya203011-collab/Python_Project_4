class StockItem:
    def __init__(self, sku, name, opening_qty):
        if opening_qty < 0:
            raise ValueError("Opening stock cannot be negative.")

        self.sku = sku
        self.name = name
        self._quantity = opening_qty

    @property
    def quantity(self):
        return self._quantity

    def dispatch(self, amount):
        if amount <= 0:
            raise ValueError("Dispatch must be positive.")

        if amount > self._quantity:
            raise ValueError("Insufficient stock.")

        self._quantity -= amount

    def __eq__(self, other):
        if not isinstance(other, StockItem):
            return NotImplemented

        return self.sku == other.sku


# Testing
item1 = StockItem("SKU-101", "Mouse", 20)
item2 = StockItem("SKU-101", "Wireless Mouse", 10)
item3 = StockItem("SKU-102", "Keyboard", 15)

print("Item 1 == Item 2:", item1 == item2)
print("Item 1 == Item 3:", item1 == item3)