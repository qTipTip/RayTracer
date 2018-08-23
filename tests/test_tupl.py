from unittest import TestCase
from src.tupl import Tupl, Point, Vector


class TestTupl(TestCase):

    def test_tupl_init(self):
        t = Tupl(1, 2, 3, 0)

        assert t.x == 1 and t.y == 2 and t.z == 3 and t.is_point() and not t.is_vector()

    def test_tupl_point(self):
        p = Point(1, 2, 3)
        assert p.is_point() and not p.is_vector()

    def test_tupl_vector(self):
        v = Vector(1, 2, 3)
        assert v.is_vector() and not v.is_point()
