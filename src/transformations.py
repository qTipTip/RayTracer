from src.matrix import IdentityMatrix


def translation(x, y, z):
    i = IdentityMatrix(4)
    i[0, 3] = x
    i[1, 3] = y
    i[2, 3] = z
    return i


def scaling(x, y, z):
    i = IdentityMatrix(4)
    i[0, 0] = x
    i[1, 1] = y
    i[2, 2] = z
    return i
