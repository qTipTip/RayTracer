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
