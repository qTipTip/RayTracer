from src.color import Color
from src.materials import DefaultMaterial


def test_default_material():
    m = DefaultMaterial()
    assert m.color == Color(1, 1, 1)
    assert m.ambient == 0.1
    assert m.diffuse == 0.9
    assert m.specular == 0.9
    assert m.shininess == 200
