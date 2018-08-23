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
