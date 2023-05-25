import pandas as pd


class ExcelReader:
    def __init__(self) -> None:
        self._path = None

    def __read_excel(self):
        return pd.ExcelFile(self._path)

    def get_data(self):
        try:
            data = self.__read_excel().parse()
            numeric_columns = data.select_dtypes(include=[float]).columns
            data[numeric_columns] = data[numeric_columns].astype(int)
            return data
        except FileNotFoundError:
            raise ValueError("La ruta es incorrecta.")

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path
