from src.egresado import Egresado


class NodoAVL:
    def __init__(self, datos: Egresado = None, izq: 'NodoAVL' = None, der: 'NodoAVL' = None, padre: 'NodoAVL' = None, f_eq: int = 0):
        self.__datos = [datos] if datos is not None else []
        self.__izq = izq
        self.__der = der
        self.__padre = padre
        self.__f_eq = f_eq

    @property
    def datos(self):
        return self.__datos

    @datos.setter
    def datos(self, datos):
        self.__datos = datos

    @property
    def izq(self):
        return self.__izq

    @izq.setter
    def izq(self, izq):
        self.__izq = izq

    @property
    def der(self):
        return self.__der

    @der.setter
    def der(self, der):
        self.__der = der

    @property
    def f_eq(self):
        return self.__f_eq

    @f_eq.setter
    def f_eq(self, f_eq):
        self.__f_eq = f_eq

    @property
    def padre(self):
        return self.__padre

    @padre.setter
    def padre(self, padre):
        self.__padre = padre

    @staticmethod
    def altura(nodo: 'NodoAVL' = None) -> int:
        if nodo is None:
            return -1
        else:
            return 1 + max(NodoAVL.altura(nodo.izq), NodoAVL.altura(nodo.der))

    def __str__(self):
        return ', '.join(str(dato) for dato in self.__datos)

    # Recorridos del árbol
    def inorden(self):
        if self.izq is not None:
            self.izq.inorden()
        for dato in self.__datos:
            print(dato, "| FE:", self.f_eq)
        if self.der is not None:
            self.der.inorden()

    def posorden(self):
        if self.izq is not None:
            self.izq.posorden()
        if self.der is not None:
            self.der.posorden()
        for dato in self.__datos:
            print(dato, "| FE:", self.f_eq)

    def preorden(self):
        for dato in self.__datos:
            print(dato, "| FE:", self.f_eq)
        if self.izq is not None:
            self.izq.preorden()
        if self.der is not None:
            self.der.preorden()
