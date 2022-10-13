import math


class pair:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"<{self.key},{self.value}>"


class aux_ret:

    def __init__(self):
        self.n_p = 0
        self.n_t = -1


class nodo:

    def __init__(self, id_i, id_padre, h, nombre):
        cod_paradas = [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 210,
                       211,
                       212,
                       213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 310, 311, 312, 314,
                       315,
                       316,
                       317, 318, 319, 321, 322, 323, 324, 325, 326, 327]
        self.id = id_i
        self.id_padre = id_padre
        self.h = h
        self.nombre = nombre
        self.total = 0
        self.g = 0
        # 0 = Rojo, 1 = Azul, 2 = Verde
        self.color = math.floor(cod_paradas[self.id]/150)

    def __str__(self):
        return f" ID: {self.id}, ID_padre: {self.id_padre}, G: {self.g}, H:  {self.h}, Total: {self.total}, Nombre: {self.nombre}"
