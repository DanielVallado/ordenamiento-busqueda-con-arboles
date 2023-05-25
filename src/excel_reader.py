import pandas as pd


class ExcelReader:
    def __init__(self) -> None:
        self._path = None

    def get_data(self):
        try:
            file = pd.ExcelFile(self._path)
            data = file.parse()
            data['Promedio'] = data['Promedio'].astype(int)
            print(data)
            return data
        except FileNotFoundError:
            raise ValueError("La ruta es incorrecta.")

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path
