import tkinter as tk
from constantes import style
from Screen import Home

class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title("Proyecto Final")
        conteiner = tk.Frame(self)
        conteiner.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )
        conteiner.configure(background = style.BACKGROUND)
        conteiner.grid_columnconfigure(0, weight = 1)
        conteiner.grid_rowconfigure(0, weight = 1)

        self.frames= {}
        #se añaden las pantallas al diccionario de frames 
        for F in (Home, ):
            frame = F(conteiner, self) 
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)#para que se pueda expandir 
        self.show_frame(Home)

    def show_frame(self, conteiner):
        frame = self.frames[conteiner]
        frame.tkraise()#lo pasa enfrente de todo,pantalla principal, por si se ponene mas pantallas 