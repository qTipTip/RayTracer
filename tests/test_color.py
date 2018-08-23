from unittest import TestCase

from src.color import Color


class TestColor(TestCase):

    def test_color__init(self):
        c = Color(12, 35, 2)

        assert c.r == 12 and c.g == 35 and c.b == 2

    def test_color_hadamard(self):
        c1 = Color(1, 2, 3)
        c2 = Color(2, 3, 4)
        c3 = Color(2, 6, 12)
        assert c1 * c2 == c3

    def test_color_scalar_mul(self):
        c1 = Color(1, 2, 3)
        c2 = Color(2, 4, 6)

        assert c1 * 2 == c2

    def test_color_str(self):
        c1 = Color(1, 2, 3)

        assert str(c1) == '1 2 3'
