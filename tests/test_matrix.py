from src.matrix import Matrix


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
