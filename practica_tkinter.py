from tkinter import Frame, Label, Scale, LEFT, HORIZONTAL

class MiVentana(Frame): 
    # Cada widget tiene un primer parámetro de constructor 
    # que es su widget 'maestro', es decir, el que lo 
    # contiene. Si no se especifica este parámetro, y si el 
    # widget en cuestión es un frame, entonces este estará 
    # contenido automáticamente en la ventana de la aplicación. 
    def __init__ (self, master = None):
       # Llamamos al constructor de la clase madre 
       # de MiVentana, es decir, Frame. Además del widget maestro, 
       # especificamos las dimensiones de la ventana, es decir, un 
       # ancho de 320 píxeles y un alto de 240. 
        super(MiVentana, self).__init__(master, width=320, height=240) 
       # La ventana que contiene el frame está referenciada por 
       # el atributo master. Entonces es él el que debe usar 
       # para modificar el título de la ventana mostrada 
       # por el sistema operativo. 
        self.master.title ("Mi Aplicación gráfica") 
 
       # pack() permite consolidar la geometría del frame 
       # en la ventana. Sin esta llamada, el dimensionamiento 
       # dado en el constructor de Frame no tendría lugar. 
        self.pack()
 
mi_ventana = MiVentana() 
mi_ventana.mainloop()

class MiVentana(Frame): 
    def __init__(self, master=None): 
        super(MiVentana, self).__init__(master) 
        self.master.title("Conversor C <-> F") 
        self.pack() 
 
    def initWidgets(self): 
        # Declaración de una etiqueta que muestra el texto 'F'. 
        # El primer argumento es el widget 'padre' 
        # que contendrá esta etiqueta, es decir, self, 
        # el frame principal. 
        self.FTexto = Label(self, text = 'F')
 
        # Declaración de un cursor que mostrará los grados 
        # Fahrenheit. Los parámetros llamados del constructor 
        # permiten personalizar el widget: su orientación 
        # es horizontal y los valores que recorre van 
        # de -148 a 212. 
        self.FCursor = Scale(self, orient=HORIZONTAL, from_=-148, 
                             to=212) 
 
        # Idem aquí para los grados Celsius. 
        self.CTexto = Label(self, text='C') 
        self.CCursor = Scale(self, orient=HORIZONTAL, from_=-100, 
                             to=100) 
 
        # Creamos una lista de widgets sobre la que hacemos un bucle ... 
        for widget in [self.CTexto, self.CCursor, self.FTexto, 
                       self.FCursor]: 
            # El widget actual está "pegado" a la izquierda 
            # en la ventana de la aplicación. 
            widget.pack(side=LEFT) 
 
# Instanciación de la ventana. 
mi_ventana = MiVentana() 
# Inicialización de los widgets. 
mi_ventana.initWidgets() 
# Lanzamiento del bucle principal. 
mi_ventana.mainloop()


class MiVentana2(Frame): 
    def __init__(self, master=None): 
        super(MiVentana2, self).__init__(master) 
        self.master.title("Conversor C <-> F") 
        self.pack() 
 
    def initWidgets(self): 
        # Declaración de una etiqueta que muestra el texto 'F'. 
        # El primer argumento es el widget 'padre' 
        # que contendrá esta etiqueta, es decir, self, 
        # el frame principal. 
        self.FTexto = Label(self, text = 'F')
 
        # Declaración de un cursor que mostrará los grados 
        # Fahrenheit. Los parámetros llamados del constructor 
        # permiten personalizar el widget: su orientación 
        # es horizontal y los valores que recorre van 
        # de -148 a 212. 
        self.FCursor = Scale(self, orient=HORIZONTAL, from_=-148, 
                             to=212, command=self.convertirFenC) 
 
        # Idem aquí para los grados Celsius. 
        self.CTexto = Label(self, text='C') 
        self.CCursor = Scale(self, orient=HORIZONTAL, from_=-100, 
                             to=100, command=self.convertirCenF)
 
        # Creamos una lista de widgets sobre la que hacemos un bucle ... 
        for widget in [self.CTexto, self.CCursor, self.FTexto, 
                       self.FCursor]: 
            # El widget actual está "pegado" a la izquierda 
            # en la ventana de la aplicación. 
            widget.pack(side=LEFT)

    # Método llamado cuando el cursor de grados Celsius 
    # se ha movido. Calcula la equivalencia en grados Fahrenheit 
    # y modifica el valor del cursor de esta escala de 
    # grados en consecuencia. 
    def convertirCenF(self, valor): 
        C = float(valor) 
        F = C * 9/5 + 32 
        self.FCursor.set(F) 

    # Como convertirCEnF(), pero en el sentido opuesto 
    # de conversión de escalas de grados. 
    def convertirFenC(self, valor): 
        F = float(valor) 
        C = (F - 32) * 5/9 
        self.CCursor.set(C)
 
# Instanciación de la ventana. 
mi_ventana = MiVentana2() 
# Inicialización de los widgets. 
mi_ventana.initWidgets() 
# Lanzamiento del bucle principal. 
mi_ventana.mainloop()