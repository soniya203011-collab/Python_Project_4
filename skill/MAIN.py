from abc import ABC, abstractmethod
import os

# =====================================================================
# [OOP CONCEPT 1: COMPOSITION ('HAS-A' RELATIONSHIP)]
# Location represents physical warehouse positioning. BaseProduct HAS-A Location.
# Decouples spatial layout tracking from pricing and stock rules.
# =====================================================================
class Location:
    def __init__(self, rack: str):
        self.rack = rack

# =====================================================================
# [OOP CONCEPT 2: ABSTRACTION & ENCAPSULATION]
# BaseProduct is an Abstract Base Class (ABC). It enforces a contract:
# all products MUST implement calc_fee(). It also encapsulates protected _stock.
# =====================================================================
class BaseProduct(ABC):
    def __init__(self, name: str, price: float, rack: str):
        self.name = name
        self.price = price
        self.loc = Location(rack)     # [COMPOSITION IN ACTION]
        self._stock = 10              # [ENCAPSULATION: Protected attribute]

    @property
    def stock(self) -> int:
        return self._stock            # Safe read-only getter

    def dispatch(self, qty: int) -> bool:
        # Invariant check: dispatch cannot exceed stock or be non-positive
        if qty <= 0 or qty > self._stock:
            raise ValueError(f'[Alert] Invalid dispatch ({qty}). Stock: {self._stock}')
        self._stock -= qty
        return True

    @abstractmethod
    def calc_fee(self, days: int) -> float:
        pass

# =====================================================================
# [OOP CONCEPT 3: INHERITANCE ('IS-A' RELATIONSHIP)]
# TechItem and FreshItem inherit attributes from BaseProduct for free
# and specialize their unique storage rate algorithms.
# =====================================================================
class TechItem(BaseProduct):
    def calc_fee(self, days: int) -> float:
        return days * 2.50  # Climate-controlled storage rate

class FreshItem(BaseProduct):
    def calc_fee(self, days: int) -> float:
        return days * 5.00  # Cold-chain refrigeration rate

# =====================================================================
# [OOP CONCEPT 4: POLYMORPHISM IN ACTION & SECURE PRACTICES]
# A single loop computes fees across diverse objects without type checks!
# =====================================================================
def main():
    api_key = os.getenv('WAREHOUSE_API_KEY', 'FALLBACK_DEV_KEY_SECURE')
    print(f'=== WAREHOUSE IMS (Auth: {api_key[:4]}****) ===')

    inventory = [
        TechItem('Laptop', 999.0, 'Aisle A-1'),
        FreshItem('Organic Milk', 4.0, 'Cold-Room B')
    ]
    print('\n--- WAREHOUSE STORAGE FEE INVENTORY REPORT ---')
    for item in inventory:
        # Polymorphism dynamically triggers correct calc_fee!
        fee = item.calc_fee(days=3)
        print(f'[{item.name}] Rack: {item.loc.rack} | 3-Day Holding Fee: ${fee:.2f}')

if __name__ == '__main__':
    main()
