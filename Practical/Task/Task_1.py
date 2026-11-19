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

    @property
    def is_in_stock(self):
        return self._quantity > 0

    def dispatch(self, amount):
        if amount <= 0:
            raise ValueError("Dispatch must be positive.")

        if amount > self._quantity:
            raise ValueError("Insufficient stock.")

        self._quantity -= amount

    def restock(self, amount):
        if amount <= 0:
            raise ValueError("Restock amount must be positive.")

        self._quantity += amount


# Testing
item = StockItem("SKU-101", "Wireless Mouse", 20)

print("Initial Stock:", item.quantity)
print("Is In Stock:", item.is_in_stock)

item.restock(10)

print("After Restocking:", item.quantity)
print("Is In Stock:", item.is_in_stock)

item.dispatch(30)

print("After Dispatch:", item.quantity)
print("Is In Stock:", item.is_in_stock)