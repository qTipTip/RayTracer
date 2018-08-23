import math
from unittest import TestCase
from src.tupl import Tupl, Point, Vector


class TestTupl(TestCase):

    def test_tupl_init(self):
        t = Tupl(1, 2, 3, 0)

        assert t.x == 1 and t.y == 2 and t.z == 3 and t.is_vector() and not t.is_point()

    def test_tupl_point(self):
        p = Point(1, 2, 3)
        assert p.is_point() and not p.is_vector()

    def test_tupl_vector(self):
        v = Vector(1, 2, 3)
        assert v.is_vector() and not v.is_point()

    def test_tupl_equality(self):
        t1 = Tupl(1, 2, 3, 0)
        t2 = Tupl(1, 2, 3, 1)
        t3 = Tupl(2, 3, 1, 2)

        assert t1 == t1 and t1 != t2 and t1 != t3

    def test_tupl_add(self):
        t1 = Tupl(3, 2, 5, 0)
        t2 = Tupl(3, 2, 1, 1)
        t3 = Tupl(6, 4, 6, 1)

        assert t1 + t2 == t3 and (t1 + t2).is_point() and (t1 + t1).is_vector()

    def test_tupl_sub(self):
        t1 = Point(3, 2, 5)
        t2 = Point(3, 2, 1)
        t3 = Vector(0, 0, 4)

        assert t1 - t2 == t3 and (t1 - t2).is_vector()

    def test_tupl_neg(self):
        t1 = Tupl(3, 2, -5, 1)
        t2 = Tupl(-3, -2, 5, -1)

        assert -t1 == t2

    def test_tupl_mul(self):
        t1 = Tupl(3, 2, -5, 1)
        t2 = Tupl(-9, -6, 15, -3)
        assert t1 * -3 == t2 and -t1 * 3 == t2

    def test_tupl_div(self):

        t1 = Tupl(3, 2, 5, 1)
        t2 = Tupl(1.5, 1, 2.5, 0.5)

        assert t1 / 2 == t2

    def test_tupl_vec_magnitude(self):

        t1 = Vector(1, 1, 1)
        eps = 1.0e-14

        assert abs(math.sqrt(3) - t1.magnitude) < eps

    def test_tupl_vec_normalize(self):

        t1 = Vector(3, 2, 5)
        eps = 1.0e-14

        n1 = t1.normalize()
        assert abs(n1.magnitude - 1) < eps