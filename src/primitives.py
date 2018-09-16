from src.matrix import IdentityMatrix


class Primitive(object):

    def __init__(self):
        self.transform = IdentityMatrix(4)

    def set_transform(self, transform):
        self.transform = transform


class Sphere(Primitive):
    pass
