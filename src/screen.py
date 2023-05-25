import os
import tkinter as tk
from tkinter import messagebox, filedialog

from constantes import style
from src.arbol_avl import ArbolAVL
from src.csv_writer import CSVWriter
from src.egresado import Egresado
from src.excel_reader import ExcelReader


class Home(tk.Frame):

    def __init__(self, parent, controller, path):
        super().__init__(parent)
        self.path = path
        self.data = None
        self.arbol_nombres = ArbolAVL()
        self.arbol_profesion = ArbolAVL()
        self.arbol_promedio = ArbolAVL()
        self.reader = ExcelReader()
        self.writer = CSVWriter()

        self.titulo_label = None
        self.texto_explicativo_label = None
        self.datos_entry = None
        self.buscar_button = None
        self.archivo_button = None
        self.spinbox = None
        self.encabezado = None
        self.lst = None

        self.configure(background=style.BACKGROUND)
        self.controller = controller

        self.introducir_archivo()

    def __init_widgets(self):
        # TITULO
        self.titulo_label = tk.Label(
            self,
            text="BÚSQUEDA DE INFORMACIÓN",
            justify=tk.CENTER,
            **style.LABEL
        )
        self.titulo_label.place(
            relx=0.25,
            rely=0.05,
            relheight=0.1,
            relwidth=0.5
        )

        # BOTÓN DE BUSCAR
        self.buscar_button = tk.Button(
            self,
            text="Buscar",
            command=self.button_clicked,
            **style.BUTTON
        )
        self.buscar_button.place(
            relx=0.60,
            rely=0.32,
            relheight=0.05,
            relwidth=.28,
        )

        # TEXTO EXPLICATIVO
        self.texto_explicativo_label = tk.Label(
            self,
            text="Introduce los datos ",
            justify=tk.LEFT,
            **style.INSTRUCCION
        )
        self.texto_explicativo_label.place(
            relx=0.08,
            rely=0.20,
            relheight=0.05,
            relwidth=0.25
        )

        # ENTRADA DE DATOS
        self.datos_entry = tk.Entry(
            self,
            justify=tk.LEFT,
            **style.ENTRADA,
        )
        self.datos_entry.place(
            relx=0.08,
            rely=0.25,
            relheight=0.05,
            relwidth=0.8
        )

        # SPINBOX
        self.spinbox = tk.Spinbox(
            self,
            values=(
                "Nombre", "Profesion", "Promedio", "Nombre y profesion", "Nombre y promedio", "Profesion y promedio"),
            justify=tk.CENTER,
            **style.SPINBOX,
        )
        self.spinbox.place(
            relx=0.08,
            rely=0.32,
            relheight=0.05,
            relwidth=0.30
        )

        # Etiqueta de encabezado
        self.encabezado = tk.Label(
            self,
            text="Nombre | Profesión | Promedio",
            justify=tk.CENTER,
            **style.LABEL
        )
        self.encabezado.place(
            relx=0.05,
            rely=0.40,
            relheight=0.05,
            relwidth=0.9
        )

        # listbox
        self.lst = tk.Listbox(
            self,
            width=50,
            **style.SPINBOX
        )
        self.lst.place(
            relx=0.05,
            rely=0.45,
            relheight=.45,
            relwidth=.90
        )

        self.exportar_button = tk.Button(
            self,
            text="Exportar en CSV",
            command=self.exportar_csv,
            **style.BUTTON
        )
        self.exportar_button.place(
            relx=0.73,
            rely=0.92,
            relheight=0.06,
            relwidth=.25,
        )

    def introducir_archivo(self):
        # Botón para leer archivo
        self.archivo_button = tk.Button(
            self,
            text="Inserte archivo Excel",
            command=self.buscar_archivo,
            **style.BUTTON
        )
        self.archivo_button.place(
            relx=0.34,
            rely=0.4,
            relheight=0.08,
            relwidth=.35,
        )

    def buscar_archivo(self):
        file_path = filedialog.askopenfilename()
        if file_path.endswith((".xls", ".xlsx")):
            self.path = file_path
            self.archivo_button.place_forget()
            self.__init_widgets()
            self.__obtener_datos()
            self.__ordenar_datos()
            self.cargar_datos(self.arbol_nombres.get_valores())
        else:
            messagebox.showerror("Error", "El archivo seleccionado no es un Excel")

    def read_entry(self):
        return self.datos_entry.get()

    def read_spinbox(self):
        return self.spinbox.get()

    def button_clicked(self):
        entrada = self.read_entry()
        tipo = self.read_spinbox()
        self.clear_table()
        self.buscar_datos(entrada, tipo)

    def add_element(self, element):
        self.lst.insert(tk.END, element)

    def clear_table(self):
        self.lst.delete(0, tk.END)

    def __obtener_datos(self):
        self.reader.path = self.path
        self.data = self.reader.get_data()

    def __ordenar_datos(self):
        columnas = self.data.iloc[:, :3]
        for fila in columnas.itertuples(index=False):
            _nombre, _profesion, _promedio = fila
            egresado = Egresado(_nombre, _profesion, int(_promedio))
            self.arbol_nombres.insertar(egresado, tipo_insercion='nombre')
            self.arbol_profesion.insertar(egresado, tipo_insercion='profesion')
            self.arbol_promedio.insertar(egresado, tipo_insercion='promedio')

    def __dividir_string(self, busqueda, parametro):
        resultado = []
        partes = busqueda.split(parametro)
        resultado[0] = partes[0].strip()
        resultado[1] = partes[1].strip()
        return resultado

    def buscar_datos(self, busqueda, tipo):
        resultado = []
        parametro = "AND"
        try:
            if tipo == 'Nombre':
                resultado = self.arbol_nombres.buscar_nombre(busqueda)
            elif tipo == 'Profesion':
                resultado = self.arbol_profesion.buscar_profesion(busqueda)
            elif tipo == 'Promedio':
                resultado = self.arbol_promedio.buscar_promedio(int(busqueda))
            elif tipo == 'Nombre y profesion':
                partes = self.__dividir_string(busqueda, parametro)
                resultado = self.arbol_nombres.buscar_nombre_profesion(partes[0], int(partes[1]))
            elif tipo == 'Nombre y promedio':
                partes = self.__dividir_string(busqueda, parametro)
                resultado = self.arbol_nombres.buscar_nombre_promedio(partes[0], partes[1])
            elif tipo == 'Profesion y promedio':
                partes = self.__dividir_string(busqueda, parametro)
                resultado = self.arbol_profesion.buscar_profesion_promedio(partes[0], int(partes[1]))
            else:
                messagebox.showerror("Error", "Tipo de búsqueda no válido")
        except ValueError:
            messagebox.showerror("Error", "El valor ingresado no es un número válido para la búsqueda por promedio")
        except IndexError:
            messagebox.showerror("Error", "Es necesario el uso de AND para búsquedas combinadas")

        self.cargar_datos(resultado)

    def cargar_datos(self, datos):
        print(self.data.to_string())
        # Agregar los datos a la tabla
        for egresado in datos:
            self.add_element(egresado)

    def exportar_csv(self):

        self.writer.path = os.path.dirname(self.path)
        self.writer.excel_to_csv(self.data, "egresados")
        messagebox.showinfo("Éxito", "¡La exportación se realizó exitosamente!")
