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

    def __eq__(self, other):

        if self.n == other.n and self.m == other.m:
            for i in range(self.n):
                for j in range(self.m):
                    if self[i, j] != other[i, j]:
                        return False
            else:
                return True
        else:
            return False

    def __matmul__(self, other):
        if self.m != other.n:
            raise ValueError('Matrix dimensions not compatible')

        elements = [
            [
                sum([self[i, k] * other[k, j] for k in range(self.n)])
                for j in range(self.n)
            ]
            for i in range(self.m)
        ]
        return Matrix(elements)
