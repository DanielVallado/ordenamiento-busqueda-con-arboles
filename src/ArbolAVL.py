from src.nodo_avl import NodoAVL
from src.egresado import Egresado


class ArbolAVL:
    def __init__(self, dato=None) -> None:
        self.__raiz = NodoAVL(datos=dato)

    @property
    def raiz(self):
        return self.__raiz

    @raiz.setter
    def raiz(self, dato):
        self.__raiz = dato

    def inorden(self):
        if self.raiz is not None:
            self.raiz.inorden()

    # ------------------Rotaciones------------------------
    def __rotacion_ii(self, nodo: NodoAVL):
        # Establecer los apuntadores..
        padre = nodo.padre
        p = nodo  # Nodo
        q = p.izq  # Nodo1
        b = q.der  # Hijo derecho de Nodo1

        # Ajustar hijos
        # Al padre de Nodo se le coloca como hijo a Nodo1 en el lugar correspondiente
        if padre is not None:
            if padre.der == p:
                padre.der = q
            else:
                padre.izq = q
        else:
            self.raiz = q
        # Reconstruir el arbol
        p.izq = b
        q.der = p
        # Reasignar Padres
        p.padre = q
        if b is not None: b.padre = p
        q.padre = padre
        # Establecer el factor de equilibrio
        p.f_eq = 0
        q.f_eq = 0

    def __rotacion_dd(self, nodo: NodoAVL):
        # Establecer los apuntadores..
        padre = nodo.padre
        p = nodo  # Nodo
        q = p.der  # Nodo1
        b = q.izq  # Hijo izquierdo de Nodo1

        # Ajustar hijos
        # Al padre de Nodo se le coloca como hijo a Nodo1 en el lugar correspondiente
        if padre is not None:
            if padre.izq == p:
                padre.izq = q
            else:
                padre.der = q
        else:
            self.raiz = q
        # Reconstruir el arbol
        p.der = b
        q.izq = p

        # Reasignar Padres
        p.padre = q
        if b is not None: b.padre = p
        q.padre = padre

        # Establecer el factor de equilibrio
        p.f_eq = 0
        q.f_eq = 0

    def __rotacion_id(self, nodo: NodoAVL):
        padre = nodo.padre
        p = nodo  # Nodo
        q = p.izq  # Nodo1
        r = q.der  # Nodo2
        b = r.izq
        c = r.der

        if padre is not None:
            if padre.der == p:
                padre.der = r
            else:
                padre.izq = r
        else:
            self.raiz = r

        # Reconstrucción del árbol
        q.der = b  # Colocar el hijo izquierdo de Nodo2 como hijo derecho de Nodo1
        p.izq = c  # Colocar el hijo derecho de Nodo2 como hijo izquierdo de Nodo
        # Colocar a Nodo1 y Nodo2 como hijos izquierdo y derecho de Nodo
        r.izq = q
        r.der = p
        # Reasignación de padres
        r.padre = padre
        p.padre = r
        q.padre = r
        if b is not None: b.padre = q
        if c is not None: c.padre = p

        # Ajusta los valores de los factores de equilibrio
        if r.f_eq == -1:  # Nodo2
            p.f_eq = 0  # Nodo
            q.f_eq = 1  # Nodo1
        elif r.f_eq == 0:
            p.f_eq = 0  # Nodo
            q.f_eq = 0  # Nodo1
        elif r.f_eq == 1:
            p.f_eq = -1  # Nodo
            q.f_eq = 0  # Nodo1
        r.f_eq = 0

    def __rotacion_di(self, nodo):
        padre = nodo.padre
        p = nodo  # Nodo
        q = p.der  # Nodo1
        r = q.izq  # Nodo2
        b = r.der
        c = r.izq

        if padre is not None:
            if padre.izq == p:
                padre.izq = r
            else:
                padre.der = r
        else:
            self.raiz = r

        # Reconstrucción del árbol
        q.izq = b  # Colocar el hijo derecho de Nodo2 como hijo izquierdo de Nodo1
        p.der = c  # Colocar el hijo izquierdo de Nodo2 como hijo derecho de Nodo
        # Colocar a Nodo1 y Nodo2 como hijos izquierdo y derecho de Nodo
        r.der = q
        r.izq = p
        # Reasignación de padres
        r.padre = padre
        p.padre = r
        q.padre = r
        if b is not None: b.padre = q
        if c is not None: c.padre = p

        # Ajusta los valores de los factores de equilibrio
        if r.f_eq == -1:  # Nodo2
            p.f_eq = 0  # Nodo
            q.f_eq = 1  # Nodo1
        elif r.f_eq == 0:
            p.f_eq = 0  # Nodo
            q.f_eq = 0  # Nodo1
        elif r.f_eq == 1:
            p.f_eq = -1  # Nodo
            q.f_eq = 0  # Nodo1
        r.f_eq = 0

    def __balancear(self, nodo: NodoAVL):
        fe_actual = nodo.f_eq
        if fe_actual == 2:
            # Determinar la rotación
            fe_hijo_der = nodo.der.f_eq
            if fe_hijo_der == 0:
                pass
            elif fe_hijo_der == 1:
                self.__rotacion_dd(nodo)
                # print("Aplicando rotación DD...")
            elif fe_hijo_der == -1:
                self.__rotacion_di(nodo)
                # print("Aplicando rotación DI...")
        else:
            fe_hijo_izq = nodo.izq.f_eq
            if fe_hijo_izq == 0:
                pass
            elif fe_hijo_izq == -1:
                self.__rotacion_ii(nodo)
                # print("Aplicando rotación II...")
            elif fe_hijo_izq == 1:
                self.__rotacion_id(nodo)
                # print("Aplicando rotación ID...")

    def __recalcular_fe(self, nodo: NodoAVL):
        if nodo is not None:
            nodo.f_eq = NodoAVL.altura(nodo.der) - NodoAVL.altura(nodo.izq)
            if abs(nodo.f_eq) == 2:
                self.__balancear(nodo)
            else:
                self.__recalcular_fe(nodo.padre)

    def __inserta_ordenado(self, nodo: NodoAVL, egresado: Egresado, criterio):
        if not nodo.datos or criterio(nodo.datos[0]) == criterio(egresado):
            nodo.datos.append(egresado)
        elif criterio(nodo.datos[0]) > criterio(egresado):
            if nodo.izq is None:
                nodo.izq = NodoAVL(egresado, None, None, nodo)
                self.__recalcular_fe(nodo)
            else:
                self.__inserta_ordenado(nodo.izq, egresado, criterio)
        elif criterio(nodo.datos[0]) < criterio(egresado):
            if nodo.der is None:
                nodo.der = NodoAVL(egresado, None, None, nodo)
                self.__recalcular_fe(nodo)
            else:
                self.__inserta_ordenado(nodo.der, egresado, criterio)

    def insertar(self, egresado: Egresado, tipo_insercion):
        if tipo_insercion == 'nombre':
            self.__inserta_ordenado(self.raiz, egresado, lambda e: e.nombre)
        elif tipo_insercion == 'profesion':
            self.__inserta_ordenado(self.raiz, egresado, lambda e: e.profesion)
        elif tipo_insercion == 'promedio':
            self.__inserta_ordenado(self.raiz, egresado, lambda e: e.promedio)

    def __buscar_arbol_ordenado(self, valor, criterio):
        nodo = self.raiz

        while nodo is not None:
            if criterio(nodo.datos[0]) == valor:
                return nodo.datos
            elif criterio(nodo.datos[0]) > valor:
                nodo = nodo.izq
            else:
                nodo = nodo.der

        return None

    def __buscar(self, nodo, valor, criterio, resultados):
        if nodo is not None:
            for egresado in nodo.datos:
                if criterio(egresado) == valor:
                    resultados.append(egresado)

            resultado_izq = self.__buscar(nodo.izq, valor, criterio, resultados)
            if resultado_izq is not None:
                return resultado_izq

            resultado_der = self.__buscar(nodo.der, valor, criterio, resultados)
            if resultado_der is not None:
                return resultado_der

        return None

    def buscar_nombre(self, nombre):
        resultados = []
        self.__buscar(self.raiz, nombre, lambda e: e.nombre, resultados)
        return resultados

    def buscar_profesion(self, profesion):
        resultados = []
        self.__buscar(self.raiz, profesion, lambda e: e.profesion, resultados)
        return resultados

    def buscar_promedio(self, promedio):
        resultados = []
        self.__buscar(self.raiz, promedio, lambda e: e.promedio, resultados)
        return resultados

    def buscar_nombre_profesion(self, nombre, profesion):
        resultado = []
        lista_egresados = self.buscar_nombre(nombre)
        for egresado in lista_egresados:
            if egresado.nombre == nombre and egresado.profesion == profesion:
                resultado.append(egresado)
        return resultado

    def buscar_nombre_promedio(self, nombre, promedio):
        resultado = []
        lista_egresados = self.buscar_nombre(nombre)
        for egresado in lista_egresados:
            if egresado.nombre == nombre and egresado.promedio == promedio:
                resultado.append(egresado)
        return resultado

    def buscar_profesion_promedio(self, profesion, promedio):
        resultado = []
        lista_egresados = self.buscar_profesion(profesion)
        for egresado in lista_egresados:
            if egresado.profesion == profesion and egresado.promedio == promedio:
                resultado.append(egresado)
        return resultado
