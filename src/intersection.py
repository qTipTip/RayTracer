class Intersection(object):

    def __init__(self, object, t):
        self.object = object
        self.t = t


class Intersections(object):
    def __init__(self, *args):
        self.objects = args

    def __len__(self):
        return len(self.objects)

    def __getitem__(self, item):
        return self.objects[item]

    def __setitem__(self, key, value):
        self.objects[key] = value
