class Item:
    def __init__(self, name, stock):
        self.name = name
        self._stock = stock  # Encapsulated state
    def dispatch(self, qty):
        if qty <= 0 or qty > self._stock:
            return False
        self._stock -= qty
        return True
    def fee(self, days):
        return days * 1.0

class ColdItem(Item):
    def fee(self, days):
        return days * 4.0  # Polymorphic override

items = [Item('Pen', 15), ColdItem('Vaccine', 5)]
reqs = [(0, 10, 2), (1, 6, 3), (1, 2, 3), (0, -5, 1)]
log = []
for idx, q, d in reqs:
    it = items[idx]
    ok = it.dispatch(q)
    cost = it.fee(d) if ok else 0.0
    log.append((it.name, ok, it._stock, cost))
print('Final Log:', log)
