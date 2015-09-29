from Vector import *


class Vector2D(Vector):
    """A vector in two dimensions.
    """

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return 'Vector2D({0}, {1})'.format(self.x, self.y)


    def __add__(self, vector):
        return Vector2D(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector):
        return Vector2D(self.x - vector.x, self.y - vector.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __div__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)


    @property
    def length(self):
        return math.hypot(self.x, self.y)

    def normalize(self):
        return Vector2D(self.x / self.length, self.y / self.length)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def distance_to(self, other):
        return math.hypot((self.x - other.x), (self.y - other.y))
