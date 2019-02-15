import math

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ("Vector (" + str(self.x) + "," + str(self.y) + ")")

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __subtract__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def scale(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        i = self.length()
        if i > 0:
             return Vector(self.x/i, self.y/i)
        else:
             return Vector(0,0)
   
