from src.transformations import translation, scaling
from src.tupl import Point, Vector


def test_translation():
    t = translation(5, -3, 2)
    p = Point(-3, 4, 5)

    assert t * p == Point(2, 1, 7)


def test_translation_inverse():
    t = translation(5, -3, 2)
    inv = t.inv
    p = Point(-3, 4, 5)

    assert inv * p == Point(-8, 7, 3)


def test_translation_vector_invariance():
    t = translation(5, -3, 2)
    v = Vector(-3, 4, 5)

    assert t * v == v


def test_scaling_point():
    t = scaling(2, 3, 4)
    p = Point(-4, 6, 8)
    assert t * p == Point(-8, 18, 32)


def test_scaling_vector():
    t = scaling(2, 3, 4)
    p = Vector(-4, 6, 8)

    assert t * p == Vector(-8, 18, 32)


def test_scaling_inverse():
    t = scaling(2, 3, 4)
    inv = t.inv
    v = Vector(-4, 6, 8)

    assert inv * v == Vector(-2, 2, 2)


def test_reflection():
    t = scaling(-1, 1, 1)
    p = Point(2, 3, 4)

    assert t * p == Point(-2, 3, 4)
