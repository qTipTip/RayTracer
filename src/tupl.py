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
        return self.w == 0

    def is_vector(self):
        return self.w == 1


class Point(Tupl):

    def __init__(self, x, y, z):
        """
        Initialize a new Point
        :param x: x-coordinate
        :param y: y-coordinate
        :param z: z-coordinate
        """
        super().__init__(x, y, z, w=0)


class Vector(Tupl):

    def __init__(self, x, y, z):
        """
        Initialize a new Vector
        :param x: x-coordinate
        :param y: y-coordinate
        :param z: z-coordinate
        """
        super().__init__(x, y, z, w=1)
