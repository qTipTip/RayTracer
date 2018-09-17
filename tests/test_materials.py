from math import sqrt

from src.color import Color
from src.lights import PointLight
from src.materials import DefaultMaterial
from src.tupl import Point, Vector


def test_default_material():
    m = DefaultMaterial()
    assert m.color == Color(1, 1, 1)
    assert m.ambient == 0.1
    assert m.diffuse == 0.9
    assert m.specular == 0.9
    assert m.shininess == 200


def test_lighting_direct():
    m = DefaultMaterial()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 0, -10), Color(1, 1, 1))

    result = m.lighting(light, position, eyev, normalv)
    assert result == Color(1.9, 1.9, 1.9)


def test_lightning_eye_angle():
    m = DefaultMaterial()
    position = Point(0, 0, 0)
    eyev = Vector(0, sqrt(2) / 2, -sqrt(2) / 2)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 0, -10), Color(1, 1, 1))

    result = m.lighting(light, position, eyev, normalv)
    assert result == Color(1.0, 1.0, 1.0)


def test_lightning_light_angle():
    m = DefaultMaterial()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, - 1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 10, -10), Color(1, 1, 1))

    result = m.lighting(light, position, eyev, normalv)
    assert result == Color(0.7363961030678927, 0.7363961030678927, 0.7363961030678927)


def test_lightning_light_and_eye_angle():
    m = DefaultMaterial()
    position = Point(0, 0, 0)
    eyev = Vector(0, -sqrt(2) / 2, - sqrt(2) / 2)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 10, -10), Color(1, 1, 1))

    result = m.lighting(light, position, eyev, normalv)
    assert result == Color(1.6363961030678928, 1.6363961030678928, 1.6363961030678928)


def test_lightning_light_behind():
    m = DefaultMaterial()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Point(0, 0, 10), Color(1, 1, 1))

    result = m.lighting(light, position, eyev, normalv)
    assert result == Color(0.1, 0.1, 0.1)
