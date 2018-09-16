from math import sqrt

from src.intersection import Intersections, Intersection
from src.tupl import Point


class Ray(object):

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def position(self, t):
        return self.origin + self.direction * t

    def intersects(self, s):
        transformed_ray = self.transform(s.transform.inv)
        obj_to_ray = transformed_ray.origin - Point(0, 0, 0)
        a = transformed_ray.direction.dot(transformed_ray.direction)
        b = 2 * transformed_ray.direction.dot(obj_to_ray)
        c = obj_to_ray.dot(obj_to_ray) - 1

        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return Intersections()
        else:
            t1 = (-b - sqrt(discriminant)) / (2 * a)
            t2 = (-b + sqrt(discriminant)) / (2 * a)
            i1 = Intersection(s, t1)
            i2 = Intersection(s, t2)
            if t1 > t2:
                return Intersections(i2, i1)
            else:
                return Intersections(i1, i2)

    def transform(self, transformation):
        return Ray(transformation * self.origin, transformation * self.direction)
