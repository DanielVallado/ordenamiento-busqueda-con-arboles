class Egresado:
    def __init__(self, nombre: str, profesion: str, promedio: int) -> None:
        self.__nombre = nombre
        self.__profesion = profesion
        self.__promedio = promedio

    def __str__(self) -> str:
        return self.__nombre + " | " + self.__profesion + " | " + str(int(self.__promedio))

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def profesion(self):
        return self.__profesion

    @profesion.setter
    def profesion(self, profesion):
        self.__profesion = profesion

    @property
    def promedio(self) -> int:
        return self.__promedio

    @promedio.setter
    def promedio(self, promedio):
        self.__promedio = promedio
