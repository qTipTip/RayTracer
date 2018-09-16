from src.color import Color


class Canvas(object):

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.pixels = [Color(0, 0, 0) for i in range(w * h)]

    def write_pixel(self, x, y, color):
        self.pixels[y * self.height + x] = color

    def __getitem__(self, ij):
        i, j = ij
        return self.pixels[j * self.height + i]

    def to_ppm(self, filename='canvas.ppm'):
        scale = 255
        header = 'P3\n {} {}\n {}\n'.format(self.width, self.height, scale)
        with open(filename, 'w') as outfile:
            outfile.write(header)
            for j in range(self.height):
                for i in range(self.width):
                    c = self[i, j]
                    r, g, b = self._format_for_ppm(c, scale)
                    outfile.write('{} {} {} '.format(r, g, b))
                outfile.write('\n ')

    def _format_for_ppm(self, c, scale):
        r, g, b = c.r, c.g, c.b
        r = max(min(scale, round(scale*r)), 0)
        g = max(min(scale, round(scale*g)), 0)
        b = max(min(scale, round(scale*b)), 0)

        return r, g, b