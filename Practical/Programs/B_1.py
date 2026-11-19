# [OOP CONCEPT: ENCAPSULATION & DATA INVARIANTS]
class StockItem:
    def __init__(self, sku: str, name: str, opening_qty: int):
        if opening_qty < 0:
            raise ValueError('[Security] Opening stock cannot be negative.')
        self.sku = sku
        self.name = name
        self._quantity = opening_qty  # Protected attribute

    @property
    def quantity(self) -> int:
        return self._quantity

    def dispatch(self, amount: int) -> bool:
        # Defensive validation prevents invalid state mutation
        if amount <= 0:
            raise ValueError('[Validation Error] Dispatch must be positive.')
        if amount > self._quantity:
            raise ValueError(f'[Stock Alert] Cannot dispatch {amount}. Available: {self._quantity}')
        self._quantity -= amount
        return True

# Verification
item = StockItem('SKU-101', 'Wireless Mouse', 20)
print('Initial Stock:', item.quantity)
item.dispatch(5)
print('After Dispatch (5):', item.quantity)
try:
    item.dispatch(25)  # Exceeds available stock
except ValueError as e:
    print('Handled Exception:', e)
print('Stock Unchanged:', item.quantity)
