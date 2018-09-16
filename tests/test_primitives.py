from src.matrix import IdentityMatrix
from src.primitives import Sphere
from src.ray import Ray
from src.transformations import translation, scaling
from src.tupl import Vector, Point


def test_sphere_default_transform():
    s = Sphere()
    assert s.transform == IdentityMatrix(4)


def test_sphere_translate():
    s = Sphere()
    t = translation(2, 3, 4)
    s.set_transform(t)

    assert s.transform == t


def test_sphere_intersection_scaled():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    s.set_transform(scaling(2, 2, 2))
    x = r.intersects(s)
    assert len(x) == 2
    assert x[0].t == 3
    assert x[1].t == 7


def test_sphere_intersection_translate():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    s.set_transform(translation(5, 0, 0))
    x = r.intersects(s)
    assert len(x) == 0
