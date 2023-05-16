import pandas as pd


class ExcelReader:
    def __init__(self) -> None:
        self.excel_file = None

    def set_path(self, path):
        self.excel_file = pd.ExcelFile(path)

    def read_excel(self):
        if self.excel_file is not None:
            return self.excel_file.parse()
        else:
            raise ValueError("No se ha establecido la ruta del archivo Excel")
