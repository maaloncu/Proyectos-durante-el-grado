from Metro import Metro
from Station import Station


def takef(elem: Station): return elem.f


class Algoritmo:
    def __init__(self, origen: Station, destino: Station, tipo, trasbordo: bool, metro: Metro):
        self.origen = origen
        self.destino = destino
        self.tipo = tipo
        self.trasbordo = trasbordo
        self.metro = metro
        self.listaabierta = []
        self.listacerrada = []
        self.posicionactual = None

    def camino(self, n1: Station, n2: Station):
        self.listacerrada.append(n1)
        if n1 is not n2:
            self.camino(n1.padre, n2)
    
    def aestrella(self):
        end = False
        error = False
        lineasorigen = self.origen.lineas
        self.listaabierta.append(self.origen)
        while not end and not error:
            if not self.listaabierta:
                print("No ha sido posible resolver el camino")
                error = True
            else:
                self.listaabierta = sorted(self.listaabierta, key=takef)
                self.posicionactual = self.listaabierta.pop(0)
                self.listacerrada.append(self.posicionactual)
                if self.posicionactual is self.destino:
                    end = True
                else:
                    for hijoposicionactual in self.metro.graph.adj[self.posicionactual]:
                        evitar = True
                        if self.destino.lineas == lineasorigen:
                            #if evitar and linea in hijoposicionactual.lineas:
                                evitar = False
                        if (not self.trasbordo and evitar) or hijoposicionactual in self.listacerrada:
                            continue
                        h = self.destino.calculoh(hijoposicionactual)
                        #Para saber si medir distancia o tiempo
                        if self.tipo == "Distancia":
                            g = self.metro.graph[self.posicionactual][hijoposicionactual]['weight'][1]
                        else:
                            g = self.metro.graph[self.posicionactual][hijoposicionactual]['weight'][0]
                        
                        #Si la estacion no esta en la lista, actualiza datos y añade
                        if hijoposicionactual not in self.listaabierta:
                            hijoposicionactual.g = self.posicionactual.g + g
                            hijoposicionactual.h = h
                            hijoposicionactual.f = hijoposicionactual.g + hijoposicionactual.h
                            hijoposicionactual.padre = self.posicionactual
                            self.listaabierta.append(hijoposicionactual)

                        elif self.posicionactual.g + g < hijoposicionactual.g:
                            hijoposicionactual.g = self.posicionactual.g + g
                            hijoposicionactual.h = h
                            hijoposicionactual.f = hijoposicionactual.g + hijoposicionactual.h
                            hijoposicionactual.padre = self.posicionactual
        self.listacerrada = []
        self.camino(self.posicionactual, self.origen)
        self.listacerrada.reverse()
        if not error:
            return [self.destino.g, self.listacerrada]
        else:
            return None
