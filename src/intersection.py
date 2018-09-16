class Intersection(object):

    def __init__(self, object, t):
        self.object = object
        self.t = t


class Intersections(object):
    def __init__(self, *args):
        self.objects = list(args)

    def __len__(self):
        return len(self.objects)

    def __getitem__(self, item):
        return self.objects[item]

    def __setitem__(self, key, value):
        self.objects[key] = value

    @property
    def hit(self):
        candidates = [i for i in self.objects if i.t >= 0]
        if len(candidates) == 0:
            return None
        return min(candidates, key=lambda i: i.t)
