# [OOP CONCEPT: COMPOSITION]
class WarehouseAisle:
    def __init__(self, aisle: str, rack: int):
        self.aisle = aisle
        self.rack = rack
    def get_pos(self) -> str:
        return f'Aisle {self.aisle}, Rack #{self.rack}'

class Pallet:
    def __init__(self, code: str, aisle: str, rack: int):
        self.code = code
        self.loc = WarehouseAisle(aisle, rack)  # Composition: Pallet HAS-A Location

# [OOP CONCEPT: OPERATOR OVERLOADING]
class Vector2D:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f'Vector2D({self.x}, {self.y})'

p = Pallet('PLT-99', 'Zone-C', 4)
print('Pallet Composed Location:', p.loc.get_pos())
v1 = Vector2D(10, 20)
v2 = Vector2D(5, 15)
print('Vector Addition (v1 + v2):', v1 + v2)
