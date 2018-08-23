class Tupl(object):

    def __init__(self, x, y, z, w):
        """
        Initialize a new Tupl
        :param x: x-coordinate
        :param y: y-coordinate
        :param z: z-coordinate
        :param w: point/vector id
        """

        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def is_point(self):
        return self.w == 1

    def is_vector(self):
        return self.w == 0

    def __eq__(self, other):
        eps = 1.0e-14
        return abs(self.x - other.x) < eps and \
               abs(self.y - other.y) < eps and \
               abs(self.z - other.z) < eps and \
               self.w == other.w


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
