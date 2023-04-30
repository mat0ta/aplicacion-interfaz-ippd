from tkinter import *
from threading import *

class MiVentana(Frame): 
    def __init__(self, master=None): 
        super(MiVentana, self).__init__(master) 
        self.master.title("Roomba calculations")
        self.pack()
 
    def initWidgets(self):
        self.Texto1 = Label(self, text = 'Ancho de la habitacion')
        self.Texto1.pack()
        self.Cursor1 = Scale(self, orient=HORIZONTAL, from_=0, 
                             to=900)
        self.Cursor1.pack()
 
        self.Texto2 = Label(self, text='Alto de la habitacion')
        self.Texto2.pack()
        self.Cursor2 = Scale(self, orient=HORIZONTAL, from_=0, 
                             to=900)
        self.Cursor2.pack()
        
        self.Texto3 = Label(self, text='Distancia del obstáculo con la pared derecha')
        self.Texto3.pack()
        self.Cursor3 = Scale(self, orient=HORIZONTAL, from_=0, 
                             to=900)
        self.Cursor3.pack()
        
        self.Texto4 = Label(self, text='Distancia del obstáculo con la pared superior')
        self.Texto4.pack()
        self.Cursor4 = Scale(self, orient=HORIZONTAL, from_=0, 
                             to=900)
        self.Cursor4.pack()
        
        self.Texto5 = Label(self, text='Ancho del cuadrado')
        self.Texto5.pack()
        self.Cursor5 = Scale(self, orient=HORIZONTAL, from_=0, 
                             to=900)
        self.Cursor5.pack()
        
        self.Texto6 = Label(self, text='Alto del cuadrado')
        self.Texto6.pack()
        self.Cursor6 = Scale(self, orient=HORIZONTAL, from_=0, 
                             to=900)
        self.Cursor6.pack()

        self.Texto7 = Label(self, text='Velocidad de limpieza (horas) por metro cuadrado del roomba')
        self.Texto7.pack()
        self.Cursor7 = Scale(self, orient=HORIZONTAL, from_=10000, 
                             to=99999)
        self.Cursor7.pack()
        
        self.Boton = Button(self, text='Calcular', command=self.sacar_roomba)
        self.Boton.pack()
 
    def sacar_roomba(self):
        # Obtener valores de los widgets
        ancho = self.Cursor1.get()
        alto = self.Cursor2.get()
        obstaculo_derecha = self.Cursor3.get()
        obstaculo_superior = self.Cursor4.get()
        ancho_cuadrado = self.Cursor5.get()
        alto_cuadrado = self.Cursor6.get()
        velocidad_m2 = self.Cursor7.get()

        # Calcular coordenadas del cuadrado verde
        x = ancho - obstaculo_derecha - ancho_cuadrado
        y = alto - obstaculo_superior - alto_cuadrado

        # Crear ventana para mostrar el cuadrado verde
        ventana2 = Toplevel(self.master)
        ventana2.title("Roomba")

        # Crear el cuadrado verde en la nueva ventana
        canvas = Canvas(ventana2, width=ancho, height=alto)
        canvas.pack()
        canvas.create_rectangle(x, y, x + ancho_cuadrado, y + alto_cuadrado, fill='green')

        #calcular el tiempo que se tarda en limpiar cada seccion del roomba y el total
        area_superior = ancho * obstaculo_superior
        area_inferior = ancho * (alto - obstaculo_superior - alto_cuadrado)
        area_izquierda = (ancho - obstaculo_derecha - ancho_cuadrado) * alto_cuadrado
        area_derecha = obstaculo_derecha * alto_cuadrado
        timepo_superior = area_superior / velocidad_m2
        timepo_inferior = area_inferior / velocidad_m2
        timepo_derecha = area_derecha / velocidad_m2
        timepo_izquierda = area_izquierda / velocidad_m2
        timepo_total = timepo_derecha+timepo_izquierda+timepo_inferior+timepo_superior

        # Borrar los widgets de la ventana principal
        self.Texto1.pack_forget()
        self.Cursor1.pack_forget()
        self.Texto2.pack_forget()
        self.Cursor2.pack_forget()
        self.Texto3.pack_forget()
        self.Cursor3.pack_forget()
        self.Texto4.pack_forget()
        self.Cursor4.pack_forget()
        self.Texto5.pack_forget()
        self.Cursor5.pack_forget()
        self.Texto6.pack_forget()
        self.Cursor6.pack_forget()
        self.Texto7.pack_forget()
        self.Cursor7.pack_forget()
        self.Boton.pack_forget()

        # Mostrar mensaje con el tiempo de limpieza en la ventana principal
        #mensaje seccion superior
        mensaje_superior = "El tiempo de limpieza de la sección superior es de {:.2f} horas".format(timepo_superior)
        Label(self, text=mensaje_superior, fg='red', font=("Arial", 14)).pack()
        #mensaje seccion inferior
        mensaje_inferior = "El tiempo de limpieza de la sección inferior es de {:.2f} horas".format(timepo_inferior)
        Label(self, text=mensaje_inferior, fg='red', font=("Arial", 14)).pack()
        #mensaje seccion derecha
        mensaje_derecha = "El tiempo de limpieza de la sección derecha es de {:.2f} horas".format(timepo_derecha)
        Label(self, text=mensaje_derecha, fg='red', font=("Arial", 14)).pack()
        #mensaje seccion izquierda
        mensaje_izquierda = "El tiempo de limpieza de la sección izquierda es de {:.2f} horas".format(timepo_izquierda)
        Label(self, text=mensaje_izquierda, fg='red', font=("Arial", 14)).pack()
        #mensaje total
        mensaje_total = "El tiempo de limpieza total es de {:.2f} horas".format(timepo_total)
        Label(self, text=mensaje_total, fg='red', font=("Arial", 14)).pack()


# Crear ventana principal
ventana = Tk()
app = MiVentana(master=ventana)
app.initWidgets()

# Iniciar ciclo de eventos
app.mainloop()