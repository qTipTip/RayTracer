import math


class Tupl(object):

    def __init__(self, x, y, z, w):
        """
        Initialize a new Tupl
        :param x: x-coordinate
        :param y: y-coordinate
        :param z: z-coordinate
        :param w: point/vector id
        """

        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = w

    def is_point(self):
        return self.w == 1

    def is_vector(self):
        return self.w == 0

    def __eq__(self, other):
        eps = 1.0e-10
        return abs(self.x - other.x) < eps and \
               abs(self.y - other.y) < eps and \
               abs(self.z - other.z) < eps and \
               abs(self.w - other.w) < eps

    def __add__(self, other):
        return Tupl(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        return Tupl(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __neg__(self):
        return Tupl(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, scalar):
        return Tupl(scalar * self.x, scalar * self.y, scalar * self.z, scalar * self.w)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * self.w

    def __truediv__(self, scalar):
        if abs(scalar) < 1.0e-16:
            raise ZeroDivisionError('Division by zero encountered in {}'.format(self.__name__))
        else:
            return Tupl(self.x / scalar, self.y / scalar, self.z / scalar, self.w / scalar)

    def __repr__(self):
        return "Tupl(x={}, y={}, z={}, w={})".format(self.x, self.y, self.z, self.w)

    @property
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        l = self.magnitude
        return Vector(self.x / l, self.y / l, self.z / l)


class Point(Tupl):

    def __init__(self, x, y, z):
        """
        Initialize a new Point
        :param x: x-coordinate
        :param y: y-coordinate
        :param z: z-coordinate
        """
        super().__init__(x, y, z, w=1)


class Vector(Tupl):

    def __init__(self, x, y, z):
        """
        Initialize a new Vector
        :param x: x-coordinate
        :param y: y-coordinate
        :param z: z-coordinate
        """
        super().__init__(x, y, z, w=0)

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.y * other.z - self.z * other.y
        )
