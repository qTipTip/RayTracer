from src.tupl import Tupl


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
        tol = 1.0e-14
        if self.n == other.n and self.m == other.m:
            for i in range(self.n):
                for j in range(self.m):
                    if not abs(self[i, j] - other[i, j]) < tol:
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

    def __mul__(self, other):

        """Matrix tuple multiplication"""
        if isinstance(other, Tupl):
            if self.m != 4:
                raise ValueError('Matrix dimensions not compatible')

            x, y, z, w = [
                sum([self[i, 0] * other.x, self[i, 1] * other.y, self[i, 2] * other.z, self[i, 3] * other.w])
                for i in range(4)
            ]
            return Tupl(x, y, z, w)
        elif isinstance(other, (float, int)):
            return Matrix([
                [other * self[i, j] for j in range(self.m)]
                for i in range(self.n)
            ])

    @property
    def T(self):
        return Matrix([
            [self[j, i] for j in range(self.m)]
            for i in range(self.n)
        ])

    def transpose(self):
        return self.T

    @property
    def determinant(self):
        if self.n == self.m == 2:
            return self[0, 0] * self[1, 1] - self[0, 1] * self[1, 0]
        else:
            return sum([self[0, j] * self.cofactor(0, j) for j in range(self.m)])

    def submatrix(self, row, col):
        return Matrix([
            [self[i, j] for j in range(self.m) if j != col]
            for i in range(self.n) if i != row
        ])

    def minor(self, row, col):
        return self.submatrix(row, col).determinant

    def cofactor(self, row, col):

        if (row + col) % 2 == 0:
            return self.minor(row, col)
        else:
            return self.minor(row, col) * -1

    @property
    def is_invertible(self):
        return self.determinant != 0


class IdentityMatrix(Matrix):
    def __init__(self, n):
        super(IdentityMatrix, self).__init__(
            [
                [int(i == j) for i in range(n)]
                for j in range(n)
            ]
        )
