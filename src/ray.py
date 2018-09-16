from math import sqrt

from src.tupl import Point


class Ray(object):

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def position(self, t):
        return self.origin + self.direction * t

    def intersects(self, s):
        obj_to_ray = self.origin - Point(0, 0, 0)
        a = self.direction.dot(self.direction)
        b = 2 * self.direction.dot(obj_to_ray)
        c = obj_to_ray.dot(obj_to_ray) - 1

        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return []
        else:
            t1 = (-b - sqrt(discriminant)) / (2 * a)
            t2 = (-b + sqrt(discriminant)) / (2 * a)
            if t1 > t2:
                return [t2, t1]
            else:
                return [t1, t2]
