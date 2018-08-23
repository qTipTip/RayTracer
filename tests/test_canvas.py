from unittest import TestCase

from src.canvas import Canvas
from src.color import Color


class TestCanvas(TestCase):

    def test_canvas_init(self):
        c = Canvas(10, 32)

        assert c.width == 10 and c.height == 32 and all([pixel == Color(0, 0, 0) for pixel in c.pixels])

    def test_canvas_write_pixel(self):
        c = Canvas(32, 32)
        col = Color(12, 3, 5)
        c.write_pixel(5, 5, col)

        assert c[5, 5] == col

    def test_canvas_get_pixel_outofbounds(self):
        c = Canvas(10, 10)
        with self.assertRaises(IndexError):
            c[100, 100]
