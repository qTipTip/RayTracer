from src.intersection import Intersection, Intersections
from src.primitives import Sphere


def test_intersection_init():
    s = Sphere()
    i = Intersection(s, 3.5)

    assert i.t == 3.5
    assert i.object == s


def test_intersection_aggregation():
    s = Sphere()
    i1 = Intersection(s, 1)
    i2 = Intersection(s, 2)
    x = Intersections(i1, i2)

    assert len(x) == 2
    assert x[0] == i1
    assert x[1] == i2


def test_hit_positive():
    s = Sphere()
    i1 = Intersection(s, 1)
    i2 = Intersection(s, 2)
    x = Intersections(i1, i2)

    h = x.hit
    assert h == i1


def test_hit_one_negative():
    s = Sphere()
    i1 = Intersection(s, -1)
    i2 = Intersection(s, 2)
    x = Intersections(i1, i2)

    h = x.hit
    assert h == i2


def test_hit_all_negative():
    s = Sphere()
    i1 = Intersection(s, -1)
    i2 = Intersection(s, -2)
    x = Intersections(i1, i2)

    h = x.hit
    assert h is None


def test_hit_always_lowest_non_negative():
    s = Sphere()
    i1 = Intersection(s, -1)
    i2 = Intersection(s, 2)
    i3 = Intersection(s, 6)
    i4 = Intersection(s, 3)
    x = Intersections(i1, i2, i3, i4)

    h = x.hit
    assert h is i2
