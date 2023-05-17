from excel_reader import ExcelReader
from arbol_avl.ArbolAVL import ArbolAVL


reader = ExcelReader()
arbol_nombres = ArbolAVL()
arbol_profesion = ArbolAVL()
arbol_promedio = ArbolAVL()

reader.set_path(r'C:\Users\danie\OneDrive - Universidad Autonoma de Yucatan\LIS\LIS - Cuarto Semestre\Estructura '
                r'de Datos\ordenamiento-busqueda-con-arboles\Egresados.xls')
data = reader.read_excel()
columnas = data.iloc[:, :3]  # Obtener las primeras tres columnas del DataFrame

for fila in columnas.itertuples(index=False):
    _nombre, _profesion, _promedio = fila
    arbol_nombres.insertar(_nombre)
    arbol_profesion.insertar(_profesion)
    arbol_promedio.insertar(int(_promedio))

arbol_promedio.inorden()
