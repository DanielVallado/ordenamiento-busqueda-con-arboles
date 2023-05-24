import os
from src.Manager import Manager
from src.arbol_avl import ArbolAVL
from src.csv_writer import CSVWriter
from src.egresado import Egresado
from src.excel_reader import ExcelReader

# Crear objetos
reader = ExcelReader()
writer = CSVWriter()
arbol_nombres = ArbolAVL()
arbol_profesion = ArbolAVL()
arbol_promedio = ArbolAVL()

# Leer datos
path = r'C:\Users\danie\OneDrive - Universidad Autonoma de Yucatan\LIS\LIS - ' \
              r'Cuarto Semestre\Estructura de Datos\ordenamiento-busqueda-con-arboles\Egresados.xls'
reader.path = path
data = reader.get_data()
columnas = data.iloc[:, :3]  # Obtener las primeras tres columnas del DataFrame

# Guardar valores
for fila in columnas.itertuples(index=False):
    _nombre, _profesion, _promedio = fila
    egresado = Egresado(_nombre, _profesion, int(_promedio))
    arbol_nombres.insertar(egresado, tipo_insercion='nombre')
    arbol_profesion.insertar(egresado, tipo_insercion='profesion')
    arbol_promedio.insertar(egresado, tipo_insercion='promedio')

arbol_promedio.inorden()

print("-----------------")
for nombre in arbol_promedio.buscar_profesion("Contador Público"):
    print(nombre)

print("-----------------")
for combinado in arbol_profesion.buscar_profesion_promedio("Licenciado en Derecho", 88):
    print(combinado)

# Creación interfaz
vista = Manager()
vista.geometry("800x600")
vista.mainloop()
# writer.path = os.path.dirname(path)
# writer.excel_to_csv(data, "egresados_en_csv")
