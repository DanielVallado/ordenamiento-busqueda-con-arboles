from excel_reader import ExcelReader
from arbol_avl.ArbolAVL import ArbolAVL
from src.egresado import Egresado

# Crear objetos
reader = ExcelReader()
arbol_nombres = ArbolAVL()
arbol_profesion = ArbolAVL()
arbol_promedio = ArbolAVL()

# Leer datos
reader.set_path(r'C:\Users\danie\OneDrive - Universidad Autonoma de Yucatan\LIS\LIS - Cuarto Semestre\Estructura '
                r'de Datos\ordenamiento-busqueda-con-arboles\Egresados.xls')
data = reader.read_excel()
columnas = data.iloc[:, :3]  # Obtener las primeras tres columnas del DataFrame

# Guardar valores
for fila in columnas.itertuples(index=False):
    _nombre, _profesion, _promedio = fila
    egresado = Egresado(_nombre, _profesion, _promedio)
    arbol_nombres.insertar(egresado, tipo_insercion='nombre')
    arbol_profesion.insertar(egresado, tipo_insercion='profesion')
    arbol_promedio.insertar(egresado, tipo_insercion='promedio')

arbol_profesion.inorden()
