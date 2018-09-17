from src.color import Color


class Material(object):
    def __init__(self, color, ambient, diffuse, specular, shininess):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess

    def __eq__(self, other):
        tol = 1.0e-14
        return self.color == other.color and abs(self.ambient - other.ambient) < tol and abs(
            self.diffuse - other.diffuse) < tol and abs(self.diffuse - other.diffuse) < tol and abs(
            self.specular - other.specular) < tol and abs(self.shininess - other.shininess) < tol

    def lighting(self, light, position, eyev, normalv):
        effective_color = self.color * light.intensity
        lightv = (light.position - position).normalize()
        ambient = effective_color * self.ambient
        light_dot_normal = lightv.dot(normalv)

        if light_dot_normal < 0:
            diffuse = Color(0, 0, 0)
            specular = Color(0, 0, 0)
        else:
            diffuse = effective_color * self.diffuse * light_dot_normal
            reflectv = -lightv.reflect(normalv)
            reflect_dot_eye = pow(reflectv.dot(eyev), self.shininess)

            if reflect_dot_eye <= 0:
                specular = Color(0, 0, 0)
            else:
                specular = light.intensity * self.specular * reflect_dot_eye
        color_vec = ambient + diffuse + specular
        return Color(color_vec.x, color_vec.y, color_vec.z)


class DefaultMaterial(Material):
    def __init__(self):
        super(DefaultMaterial, self).__init__(Color(1, 1, 1), 0.1, 0.9, 0.9, 200)
