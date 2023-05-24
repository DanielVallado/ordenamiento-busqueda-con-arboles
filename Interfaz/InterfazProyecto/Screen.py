import tkinter as tk
from constantes import style

class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller
        #para guarda la info, mapearlo 
        #self.safeInfo = tk.StringVar(self, value = ?)
        self.init_widgets()
        self.init_tabla()
        

    def init_widgets(self):
        #TITULO
        tk.Label(
            self,
            text = "Búsqueda de información",
            justify = tk.CENTER,
            **style.LABEL #MANDAMOS EL DICCIONARIO DE "STYLE"
            ).place(
            relx = 0.25,
            rely = 0.05,
            relheight =0.1,
            relwidth = 0.5,#ancho 
            ) 
        #BOTON DE BUSACR
        tk.Button(
            self,
            text = "Buscar",
            **style.BUTTON
            ).place(
                relx = 0.35,
                rely = 0.45,
                relheight = 0.1,
                relwidth = .28,
                )
        #TEXTO EXPLICATIVO
        tk.Label(
            self,
            text = "Introduce los datos ",
            justify = tk.LEFT,
            **style.INSTRUCCION 
            ).place(
            relx = 0.1,
            rely = 0.25,
            relheight =0.05,
            relwidth = 0.25,#ancho             
            ) 
        #ENTRADA DE DATOS 
        tk.Entry(
            self,
            justify = tk.LEFT,
            **style.ENTRADA,
        ).place(
            relx = 0.1,
            rely = 0.35,
            relheight =0.05,
            relwidth = 0.5,#ancho            
        )
        #TEXTO EXPLICATIVO
        tk.Label(
            self,
            text = "Filtrar por: ",
            justify = tk.LEFT,
            **style.INSTRUCCION 
            ).place(
            relx = 0.60,
            rely = 0.25,
            relheight =0.05,
            relwidth = 0.25,#ancho             
            ) 
        #spingbox 
        tk.Spinbox(
            self,
            values =("Nombre", "Profesión", "Promedio", "Nombre y profesión", "Nombre y promedio", "Profesión y nombre", "Profesión y promedio"),
            justify = tk.CENTER,
            **style.SPINGBOX,
        ).place(
            relx = 0.65,
            rely = 0.35,
            relheight =0.05,
            relwidth = 0.30,#ancho  
        )  

    def init_tabla(self):
        #listbox
        lst = tk.Listbox(
            self,
            width = 50,
            **style.SPINGBOX
        )
        lst.place(
            relx = 0.2,
            rely = 0.60,
            relheight=.35,
            relwidth=.60
        )
        lst.insert(0,"Mariam")



               
    

         
  
        
        
        