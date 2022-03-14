import math

class Point():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distance_to(self, other: "Point") -> float:
        return math.sqrt(
            (self.x - other.x) ** 2 + 
            (self.y - other.y) ** 2)
