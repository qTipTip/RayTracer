from src.materials import DefaultMaterial
from src.matrix import IdentityMatrix
from src.tupl import Point


class Primitive(object):

    def __init__(self):
        self.transform = IdentityMatrix(4)
        self.origin = Point(0, 0, 0)
        self.material = DefaultMaterial()

    def set_transform(self, transform):
        self.transform = transform

    def set_material(self, m):
        self.material = m


class Sphere(Primitive):

    def normal_at(self, point):
        object_point = self.transform.inv * point
        object_normal = object_point - self.origin
        world_normal = self.transform.inv.T * object_normal
        world_normal.w = 0
        return world_normal.normalize()
