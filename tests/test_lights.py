from src.color import Color
from src.lights import PointLight
from src.tupl import Point


def test_point_light_init():
    c = Color(1, 1, 1)
    p = Point(0, 0, 0)

    l = PointLight(p, c)
