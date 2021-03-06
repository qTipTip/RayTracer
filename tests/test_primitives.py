from math import sqrt

from src.color import Color
from src.materials import DefaultMaterial, Material
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


def test_sphere_normal_at_x():
    s = Sphere()
    n = s.normal_at(Point(1, 0, 0))

    assert n == Vector(1, 0, 0)


def test_sphere_normal_at_y():
    s = Sphere()
    n = s.normal_at(Point(0, 1, 0))
    assert n == Vector(0, 1, 0)


def test_sphere_normal_at_z():
    s = Sphere()
    n = s.normal_at(Point(0, 0, 1))
    assert n == Vector(0, 0, 1)


def test_sphere_normal_at_arbitrary():
    s = Sphere()
    n = s.normal_at(Point(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3))

    assert n == Vector(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3)


def test_sphere_normal_normalized():
    s = Sphere()
    n = s.normal_at(Point(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3))

    assert n == n.normalize()


def test_sphere_normal_at_translate():
    s = Sphere()
    s.set_transform(translation(0, 1, 0))
    n = s.normal_at(Point(0, 1.70711, -0.70711))
    assert n == Vector(0, 0.7071067811865475, -0.7071067811865476)


def test_sphere_normal_at_scaled():
    s = Sphere()
    s.set_transform(scaling(1, 0.5, 1))
    n = s.normal_at(Point(0, sqrt(2) / 2, -sqrt(2) / 2))
    assert n == Vector(0, 0.9701425001453319, -0.24253562503633297)


def test_sphere_material():
    s = Sphere()
    m = s.material

    assert m == DefaultMaterial()


def test_sphere_material_assignment():
    s = Sphere()
    m = Material(Color(1, 1, 1), 2, 1, 0.5, 12)

    s.set_material(m)
    assert s.material == m
