import tkinter as tk
from constantes import style
from Screen import Home


class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Proyecto Final")
        container = tk.Frame(self)

        container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )

        container.configure(background=style.BACKGROUND)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        # Se añaden las pantallas al diccionario de frames
        for F in (Home,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)  # Para que se pueda expandir
        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()  # Lo pasa enfrente de todos (pantalla principal) por si se ponen más pantallas
