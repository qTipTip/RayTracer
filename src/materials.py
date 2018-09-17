from src.color import Color


class Material(object):
    def __init__(self, color, ambient, diffuse, specular, shininess):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess

    def __eq__(self, other):
        tol = 1.0e-14
        return self.color == other.color and abs(self.ambient - other.ambient) < tol and abs(
            self.diffuse - other.diffuse) < tol and abs(self.diffuse - other.diffuse) < tol and abs(
            self.specular - other.specular) < tol and abs(self.shininess - other.shininess) < tol


class DefaultMaterial(Material):
    def __init__(self):
        super(DefaultMaterial, self).__init__(Color(1, 1, 1), 0.1, 0.9, 0.9, 200)
