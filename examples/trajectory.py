from src.canvas import Canvas
from src.color import Color
from src.tupl import Vector, Point


def tick(p, v):
    p += v
    v += Vector(0, -0.1, 0) + Vector(-0.01, 0, 0)
    return p, v


c = Canvas(900, 550)
col = Color(255, 255, 255)

if __name__ == '__main__':
    p = Point(0, 1, 0)
    v = Vector(1, 1.8, 0).normalize() * 11.25

    for i in range(100):
        X = int(p.x)
        Y = int(p.y)

        if p.y <= 0:
            break
        if (0 <= X < c.width) and (0 <= c.height - Y < c.height):
            c.write_pixel(X, c.height - Y, col)
        p, v = tick(p, v)

    c.to_ppm('trajectory.ppm')
