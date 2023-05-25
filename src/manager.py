import tkinter as tk

from constantes import style
from src.screen import Home


class Manager(tk.Tk):
    def __init__(self, path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Proyecto Final")

        # Obtener el tamaño de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        window_width = 800  # Ancho deseado de la ventana
        window_height = 600  # Alto deseado de la ventana
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Establecer las coordenadas de la ventana
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        container = tk.Frame(self)

        container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )

        container.configure(background=style.BACKGROUND)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        # Crear la pantalla Home
        self.home = Home(container, self, path)
        self.home.grid(row=0, column=0, sticky=tk.NSEW)  # Para que se pueda expandir
        self.show_home()

    def show_home(self):
        self.home.tkraise()

