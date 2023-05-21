import os


class CSVWriter:
    def __init__(self) -> None:
        self.path = None

    def excel_to_csv(self, data, nombre_archivo):
        nombre_archivo = os.path.join(self.path, nombre_archivo + ".csv")
        print(nombre_archivo)
        data.to_csv(nombre_archivo, index=False, sep=',')
        print("Archivo exportado en CSV")

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path
