import math


class Station:
    def __init__(self, name, lat, long, lineas):
        self.name = name
        self.lat = lat
        self.long = long
        self.lineas = lineas
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.padre = None

    def calculoh(self, nodo):
        r = 6371.0
        latituddestino = math.radians(self.lat)
        longituddestino = math.radians(self.long)
        latitudnodo = math.radians(nodo.lat)
        longitudnodo = math.radians(nodo.long)
        dlatitud = latitudnodo - latituddestino
        dlongitud = longitudnodo - longituddestino
        a = math.sin(dlatitud / 2) ** 2 + math.cos(latituddestino) * math.cos(latitudnodo) * math.sin(
            dlongitud / 2) ** 2
        b = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return r * b
