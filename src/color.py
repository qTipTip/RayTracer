from src.tupl import Tupl


class Color(Tupl):
    def __init__(self, red, green, blue):
        super().__init__(red, green, blue, 0)

    @property
    def r(self):
        return self.x

    @property
    def g(self):
        return self.y

    @property
    def b(self):
        return self.z

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return super().__mul__(other)
        else:
            return Color(self.r * other.r, self.g * other.g, self.b * other.b)
