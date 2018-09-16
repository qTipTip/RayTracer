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

    assert A.determinant == 17


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


def test_matrix_minor_3x3():
    A = Matrix([
        [3, 5, 0],
        [2, -1, -7],
        [6, -1, 5]
    ])
    b = A.submatrix(1, 0)

    assert b.determinant == 25
    assert A.minor(1, 0) == 25


def test_matrix_cofactor_3x3():
    A = Matrix([
        [3, 5, 0],
        [2, -1, -7],
        [6, -1, 5]
    ])

    assert A.minor(0, 0) == -12
    assert A.cofactor(0, 0) == -12
    assert A.minor(1, 0) == 25
    assert A.cofactor(1, 0) == -25


def test_matrix_determinant_3x3():
    A = Matrix([
        [1, 2, 6],
        [-5, 8, -4],
        [2, 6, 4]
    ])

    assert A.cofactor(0, 0) == 56
    assert A.cofactor(0, 1) == 12
    assert A.cofactor(0, 2) == -46
    assert A.determinant == -196


def test_matrix_determinant_4x4():
    A = Matrix([
        [-2, -8, 3, 5],
        [-3, 1, 7, 3],
        [1, 2, -9, 6],
        [-6, 7, 7, -9]
    ])

    assert A.cofactor(0, 0) == 690
    assert A.cofactor(0, 1) == 447
    assert A.cofactor(0, 2) == 210
    assert A.cofactor(0, 3) == 51
    assert A.determinant == -4071


def test_matrix_invertable():
    A = Matrix([
        [6, 4, 4, 4],
        [5, 5, 7, 6],
        [4, -9, 3, -7],
        [9, 1, 7, -6]
    ])

    assert A.determinant == -2120
    assert A.is_invertible


def test_matrix_non_invertable():
    A = Matrix([
        [-4, 2, -2, -3],
        [9, 6, 2, 6],
        [0, -5, 1, -5],
        [0, 0, 0, 0]
    ])
    assert A.determinant == 0
    assert not A.is_invertible


def test_matrix_inverse_4x4():
    A = Matrix([
        [-5, 2, 6, -8],
        [1, -5, 1, 8],
        [7, 7, -6, -7],
        [1, -3, 7, 4]
    ])
    B = A.inv

    assert A.determinant == 532
    assert A.cofactor(2, 3) == -160
    assert B[3, 2] == -160 / 532
    assert A.cofactor(3, 2) == 105
    assert B[2, 3] == 105 / 532

    assert B == Matrix([
        [0.21805, 0.45113, 0.24060, -0.04511],
        [-0.80827, -1.45677, -0.44361, 0.52068],
        [-0.07895, -0.22368, -0.05263, 0.19737],
        [-0.52256, -0.81391, -0.30075, 0.30639]
    ])


def test_matrix_inverse_4x4_two():
    A = Matrix([
        [8, -5, 9, 2],
        [7, 5, 6, 1],
        [-6, 0, 9, 6],
        [-3, 0, -9, -4]
    ])
    assert A.inv == Matrix([
        [-0.15385, -0.15385, -0.28205, -0.53846],
        [-0.07692, 0.12308, 0.02564, 0.03077],
        [0.35897, 0.35897, 0.43590, 0.92308],
        [-0.69231, -0.69231, -0.76923, -1.92308]
    ])
