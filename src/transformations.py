from math import cos, sin

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


def rotation_x(r):
    i = IdentityMatrix(4)
    i[1, 1] = cos(r)
    i[2, 2] = cos(r)
    i[1, 2] = -sin(r)
    i[2, 1] = sin(r)
    return i


def rotation_y(r):
    i = IdentityMatrix(4)
    i[0, 0] = cos(r)
    i[2, 2] = cos(r)
    i[2, 0] = -sin(r)
    i[0, 2] = sin(r)
    return i


def rotation_z(r):
    i = IdentityMatrix(4)
    i[0, 0] = cos(r)
    i[1, 1] = cos(r)
    i[0, 1] = -sin(r)
    i[1, 0] = sin(r)
    return i
