from math import pi

from src.canvas import Canvas
from src.color import Color
from src.transformations import rotation_z
from src.tupl import Point

c = Canvas(400, 400)
origin = Point(0, 0, 0)
r = pi / 6

hand = Point(0, 1, 0) * c.height * (3 / 8)
t = rotation_z(r)
for i in range(12):
    X, Y = int(hand.x + c.width / 2), int(hand.y + c.height / 2)
    c.write_pixel(X, Y, Color(255, 255, 255))
    hand = t * hand
c.to_ppm('clock.ppm')
