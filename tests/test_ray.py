from src.ray import Ray
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
