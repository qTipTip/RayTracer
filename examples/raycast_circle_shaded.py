from src.canvas import Canvas
from src.color import Color
from src.lights import PointLight
from src.primitives import Sphere
from src.ray import Ray
from src.tupl import Point

s = Sphere()

r_origin = Point(0, 0, -5)
wall_z = 10
wall_size = 7

light_position = Point(-10, 10, 10)
light_color = Color(1, 1, 1)
light = PointLight(light_position, light_color)

N = 200
c = Canvas(N, N)
pixel_size = wall_size / N
half = wall_size / 2

for y in range(c.height):
    world_y = half - pixel_size * y
    for x in range(c.width):
        world_x = -half + pixel_size * x
        position = Point(world_x, world_y, wall_z)
        r = Ray(r_origin, (position - r_origin).normalize())
        X = r.intersects(s)
        if X.hit is not None:
            point = r.position(X.hit.t)
            normal = X.hit.object.normal_at(point)
            eye = -r.direction
            color = X.hit.object.material.lighting(light, point, eye, normal)
            c.write_pixel(x, y, color)
c.to_ppm('circle_shaded.ppm')
