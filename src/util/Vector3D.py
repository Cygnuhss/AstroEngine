from Vector import *


class Vector3D(Vector):
    """A vector in three dimensions.
    """

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return 'Vector3D({0}, {1}, {2})'.format(self.x, self.y, self.z)


    def __add__(self, vector):
        return Vector3D(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def __sub__(self, vector):
        return Vector3D(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __div__(self, scalar):
        return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)


    @property
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalize(self):
        return Vector3D(self.x / self.length, self.y / self.length, self.z / self.length)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def distance_to(self, other):
        return math.hypot((self.x - other.x), (self.y - other.y), (self.z - other.z))
