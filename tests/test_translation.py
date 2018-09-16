from src.translations import translation
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
