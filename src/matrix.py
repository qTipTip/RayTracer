class Matrix(object):

    def __init__(self, elements):
        self.elements = elements

        if len(elements) == 0:
            raise ValueError('Cannot create matrix with no elements')
        self.n = len(elements)
        self.m = len(elements[0])

    def __getitem__(self, item):
        i, j = item
        return self.elements[i][j]
