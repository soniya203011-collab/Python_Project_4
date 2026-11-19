from abc import ABC, abstractmethod

# [OOP CONCEPT: ABSTRACTION]
class BaseProduct(ABC):
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price

    @abstractmethod
    def calc_daily_storage_fee(self, days: int) -> float:
        pass

# [OOP CONCEPT: INHERITANCE]
class TechProduct(BaseProduct):
    def calc_daily_storage_fee(self, days: int) -> float:
        return days * 2.50  # Climate control rate

class FreshProduct(BaseProduct):
    def calc_daily_storage_fee(self, days: int) -> float:
        return days * 5.00  # Refrigerated storage rate

# [OOP CONCEPT: POLYMORPHISM IN ACTION]
catalog = [TechProduct('Laptop', 800.0), FreshProduct('Berries', 5.0)]
print('--- POLYMORPHIC FEE REPORT (3 Days) ---')
for p in catalog:
    fee = p.calc_daily_storage_fee(3)
    print(f'{p.name} ({type(p).__name__}) Storage Fee: Rs.{fee:.2f}')
