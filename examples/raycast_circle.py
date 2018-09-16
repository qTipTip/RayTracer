from src.canvas import Canvas
from src.color import Color
from src.primitives import Sphere
from src.ray import Ray
from src.tupl import Point

s = Sphere()
r_origin = Point(0, 0, -5)
wall_z = 10
wall_size = 7

N = 100
c = Canvas(N, N)
pixel_size = wall_size / N
half = wall_size / 2
red = Color(255, 0, 0)

for y in range(c.height):
    world_y = half - pixel_size * y
    for x in range(c.width):
        world_x = -half + pixel_size * x
        position = Point(world_x, world_y, wall_z)
        r = Ray(r_origin, (position - r_origin).normalize())
        X = r.intersects(s)
        if X.hit is not None:
            c.write_pixel(x, y, red)
c.to_ppm('circle.ppm')
