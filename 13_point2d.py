import math


class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print(f"Point({self.x}, {self.y})")

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


p1 = Point2D(1, 2)
p2 = Point2D(4, 6)
p1.display()
p2.display()
print("Distance between points:", p1.distance(p2))
print("Distance of p2 from origin:", p2.distance_from_origin())
