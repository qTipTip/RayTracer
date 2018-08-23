from src.color import Color


class Canvas(object):

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.pixels = [Color(0, 0, 0) for i in range(w * h)]

    def write_pixel(self, x, y, color):
        self.pixels[x * self.width + y] = color

    def __getitem__(self, ij):
        i, j = ij
        return self.pixels[i * self.width + j]

    def to_ppm(self, filename='canvas.ppm'):
        pass
