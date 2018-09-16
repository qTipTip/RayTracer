import os
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
        c.write_pixel(2, 3, col)

        assert c[2, 3] == col

    def test_canvas_get_pixel_outofbounds(self):
        c = Canvas(10, 10)
        with self.assertRaises(IndexError):
            c[100, 100]

    def test_canvas_to_ppm_header(self):
        c = Canvas(5, 3)
        outfile = 'test_canvas_to_ppm_header.ppm'
        c.to_ppm(outfile)
        with open(outfile, 'r') as infile:
            assert 'P3' in infile.readline()
            assert '5 3' in infile.readline()
            assert '255' in infile.readline()
        try:
            os.remove(outfile)
        except FileNotFoundError:
            pass

    def test_canvas_to_ppm_body(self):
        c = Canvas(5, 3)
        c1 = Color(1.5, 0, 0)
        c2 = Color(0, 0.5, 0)
        c3 = Color(-0.5, 0, 1)

        c.write_pixel(0, 0, c1)
        c.write_pixel(2, 1, c2)
        c.write_pixel(4, 2, c3)

        outfile = 'test_canvas_to_ppm_body.ppm'
        c.to_ppm(outfile)

        with open(outfile, 'r') as infile:
            [infile.readline() for i in range(3)]  # skip header
            body = list(map(str.strip, infile.readlines()))
            l1 = "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
            l2 = "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0"
            l3 = "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"
            assert body[0] == l1
            assert body[1] == l2
            assert body[2] == l3
        try:
            os.remove(outfile)
        except FileNotFoundError:
            pass
