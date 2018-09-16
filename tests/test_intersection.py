from src.intersection import Intersection, Intersections
from src.primitives import Sphere


def test_intersection_init():
    s = Sphere()
    i = Intersection(s, 3.5)

    assert i.t == 3.5
    assert i.object == s


def test_intserction_aggregation():
    s = Sphere()
    i1 = Intersection(s, 1)
    i2 = Intersection(s, 2)
    x = Intersections(i1, i2)

    assert len(x) == 2
    assert x[0] == i1
    assert x[1] == i2
