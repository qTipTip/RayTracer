from src.primitives import Sphere
from src.ray import Ray
from src.transformations import translation, scaling
from src.tupl import Point, Vector


def test_ray_init():
    origin = Point(1, 2, 3)
    direct = Vector(4, 5, 6)

    r = Ray(origin, direct)
    assert r.origin == origin
    assert r.direction == direct


def test_ray_position():
    r = Ray(Point(2, 3, 4), Vector(1, 0, 0))

    assert r.position(0) == Point(2, 3, 4)
    assert r.position(1) == Point(3, 3, 4)
    assert r.position(-1) == Point(1, 3, 4)
    assert r.position(2.5) == Point(4.5, 3, 4)


def test_ray_intersect_sphere_middle():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    x = r.intersects(s)

    assert len(x) == 2
    assert x[0].t == 4
    assert x[1].t == 6


def test_ray_intersect_sphere_tangent():
    r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
    s = Sphere()
    x = r.intersects(s)

    assert len(x) == 2
    assert x[0].t == 5
    assert x[1].t == 5


def test_ray_intersect_sphere_no_intersection():
    r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
    s = Sphere()
    x = r.intersects(s)

    assert len(x) == 0


def test_ray_intersect_from_middle():
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    s = Sphere()
    x = r.intersects(s)

    assert len(x) == 2
    assert x[0].t == -1
    assert x[1].t == 1


def test_ray_intersect_from_behind():
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
    s = Sphere()
    x = r.intersects(s)

    assert len(x) == 2
    assert x[0].t == -6
    assert x[1].t == -4


def test_ray_intersects_sphere_object():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    x = r.intersects(s)

    assert len(x) == 2
    assert x[0].object == s
    assert x[1].object == s


def test_translate():
    r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
    m = translation(3, 4, 5)
    r2 = r.transform(m)
    assert r2.origin == Point(4, 6, 8)
    assert r2.direction == Vector(0, 1, 0)


def test_scale():
    r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
    m = scaling(2, 3, 4)
    r2 = r.transform(m)
    assert r2.origin == Point(2, 6, 12)
    assert r2.direction == Vector(0, 3, 0)
