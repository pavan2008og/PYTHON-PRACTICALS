import math


class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print(f"Point({self.x}, {self.y})")


class Point3D(Point2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def display(self):
        print(f"Point({self.x}, {self.y}, {self.z})")

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 +
                         (self.y - other.y) ** 2 +
                         (self.z - other.z) ** 2)


a = Point3D(1, 2, 3)
b = Point3D(4, 6, 8)
a.display()
b.display()
print("3D distance:", b.distance(a))
