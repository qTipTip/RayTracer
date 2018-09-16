from math import pi, sqrt

from src.transformations import translation, scaling, rotation_x, rotation_y, rotation_z, shearing
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


def test_rotation_x_axis():
    p = Point(0, 1, 0)
    h_q = rotation_x(pi / 4)
    f_q = rotation_x(pi / 2)

    assert h_q * p == Point(0, sqrt(2) / 2, sqrt(2) / 2)
    assert f_q * p == Point(0, 0, 1)


def test_rotation_x_axis_inverse():
    p = Point(0, 1, 0)
    h_q = rotation_x(pi / 4)
    inv = h_q.inv

    assert inv * p == Point(0, sqrt(2) / 2, -sqrt(2) / 2)


def test_rotation_y_axis():
    p = Point(0, 0, 1)
    h_q = rotation_y(pi / 4)
    h_f = rotation_y(pi / 2)

    assert h_q * p == Point(sqrt(2) / 2, 0, sqrt(2) / 2)
    assert h_f * p == Point(1, 0, 0)


def test_rotation_z_axis():
    p = Point(0, 1, 0)
    h_q = rotation_z(pi / 4)
    h_f = rotation_z(pi / 2)

    assert h_q * p == Point(-sqrt(2) / 2, sqrt(2) / 2, 0)
    assert h_f * p == Point(-1, 0, 0)


def test_shearing_x_y():
    t = shearing(1, 0, 0, 0, 0, 0)
    p = Point(2, 3, 4)

    assert t * p == Point(5, 3, 4)


def test_shearing_x_z():
    t = shearing(0, 1, 0, 0, 0, 0)
    p = Point(2, 3, 4)

    assert t * p == Point(6, 3, 4)


def test_shearing_y_x():
    t = shearing(0, 0, 1, 0, 0, 0)
    p = Point(2, 3, 4)
    assert t * p == Point(2, 5, 4)


def test_shearing_y_z():
    t = shearing(0, 0, 0, 1, 0, 0)
    p = Point(2, 3, 4)
    assert t * p == Point(2, 7, 4)


def test_shearing_z_x():
    t = shearing(0, 0, 0, 0, 1, 0)
    p = Point(2, 3, 4)
    assert t * p == Point(2, 3, 6)


def test_shearing_z_y():
    t = shearing(0, 0, 0, 0, 0, 1)
    p = Point(2, 3, 4)
    assert t * p == Point(2, 3, 7)


def test_transformation_chain():
    p = Point(1, 0, 1)
    A = rotation_x(pi / 2)
    B = scaling(5, 5, 5)
    C = translation(10, 5, 7)
    T = C @ B @ A

    assert T * p == Point(15, 0, 7)
