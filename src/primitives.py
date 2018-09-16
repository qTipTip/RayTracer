from src.matrix import IdentityMatrix
from src.tupl import Point


class Primitive(object):

    def __init__(self):
        self.transform = IdentityMatrix(4)
        self.origin = Point(0, 0, 0)

    def set_transform(self, transform):
        self.transform = transform


class Sphere(Primitive):

    def normal_at(self, point):
        return (point - self.origin).normalize()
