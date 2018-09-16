from src.matrix import Matrix, IdentityMatrix
from src.tupl import Tupl


def test_matrix():
    M = Matrix([
        [1, 2, 3, 4],
        [5.5, 6.5, 7.5, 8.5],
        [9, 10, 11, 12],
        [13.5, 14.5, 15.5, 16.5]
    ])

    assert M[0, 0] == 1
    assert M[1, 0] == 5.5
    assert M[2, 0] == 9
    assert M[3, 3] == 16.5
    assert M[3, 2] == 15.5


def test_matrix_multiplication():
    A = Matrix([
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6],
        [4, 5, 6, 7]
    ])
    B = Matrix([
        [0, 1, 2, 4],
        [1, 2, 4, 8],
        [2, 4, 8, 16],
        [4, 8, 16, 32]
    ])
    C = Matrix([
        [24, 49, 98, 196],
        [31, 64, 128, 256],
        [38, 79, 158, 316],
        [45, 94, 188, 376]
    ])

    assert A @ B == C


def test_matrix_tuple_multiplication():
    A = Matrix([
        [1, 2, 3, 4],
        [2, 4, 4, 2],
        [8, 6, 4, 1],
        [0, 0, 0, 1]
    ])
    b = Tupl(1, 2, 3, 1)
    assert A * b == Tupl(18, 24, 33, 1)


def test_matrix_identity():
    A = Matrix([
        [1, 2, 3, 4],
        [2, 4, 4, 2],
        [8, 6, 4, 1],
        [0, 0, 0, 1]
    ])

    I = IdentityMatrix(4)

    assert A @ I == A and I @ A == A


def test_matrix_transpose():
    A = Matrix([
        [1, 2, 3, 4],
        [2, 4, 4, 2],
        [8, 6, 4, 1],
        [0, 0, 0, 1]
    ])

    AT = Matrix([
        [1, 2, 8, 0],
        [2, 4, 6, 0],
        [3, 4, 4, 0],
        [4, 2, 1, 1]
    ])
    assert A.T == AT


def test_matrix_indentity_transpose():
    I = IdentityMatrix(10)
    assert I == I.T


def test_matrix_determinant_2x2():
    A = Matrix([
        [1, 5],
        [-3, 2]
    ])

    assert A.determinant() == 17


def test_matrix_submatrix_3x3():
    A = Matrix([
        [1, 5, 0],
        [-3, 2, 7],
        [0, 6, -3]
    ])
    a = A.submatrix(0, 2)
    assert a.n == 2 and a.m == 2
    assert a == Matrix([
        [-3, 2],
        [0, 6]
    ])


def test_matrix_submatrix_4x4():
    A = Matrix([
        [-6, 1, 1, -6],
        [3, 2, 5, 1],
        [2, 1, -2, 3],
        [1, 5, 2, 7]
    ])
    a = A.submatrix(0, 3)

    assert a.n == 3 and a.m == 3
    assert a == Matrix([
        [3, 2, 5],
        [2, 1, -2],
        [1, 5, 2]
    ])
