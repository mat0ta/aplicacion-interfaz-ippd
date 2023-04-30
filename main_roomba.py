from tkinter import *
from threading import *
from time import sleep
'''
class Roomba():
    def __init__(self, master, x, y, room_x=100, room_y=100, obstacles_number=1):
        self.master = master
        self.master.title("Roomba drawing")
        self.room = Canvas(self.master,
            width=room_x,
            height=room_y,
            bg="white"
        )

        self.cleaned = []
        self.obstacles = [[x, y, room_x - x, room_y - y]]
        self.room.create_rectangle(x, y, room_x - x, room_y - y, fill="green")
        self.roomba = self.room.create_oval(1, 1, 10, 10, fill="red")
        self.actual_x = 1
        self.actual_y = 1
        self.master.update()
        self.room.update()
        self.room.pack()
        while True:
            self.initiate()
            mainloop()
            sleep(30)
            break
    
    def move(self, x, y):
        if not self.detect_obstacle(self.actual_x + x, self.actual_x + y):
            self.room.move(self.roomba, x, y)
            self.clean()
            self.actual_x += x
            self.actual_y += y
        self.master.update()
        self.room.update()
        sleep(0.01)
    
    def move_up(self):
        self.move(0, -1)
    
    def move_down(self):
        self.move(0, 1)
    
    def move_left(self):
        self.move(-1, 0)
    
    def move_right(self):
        self.move(1, 0)
    
    def detect_obstacle(self, x, y):
        for i in range(len(self.obstacles)):
            if self.obstacles[i][0] <= x <= self.obstacles[i][2] and self.obstacles[i][1] <= y <= self.obstacles[i][3]:
                return True
        return False
    
    def update_section(self, x, y):
        self.cleaned.append([x, y])
    
    def clean(self):
        x, y = self.actual_x, self.actual_y
        if [x, y] not in self.cleaned:
            self.update_section(x, y)
            self.master.update()
            self.room.update()
            self.room.pack()
    
    def initiate(self):
        x, y, z, w = [], [], [], []
        for i in range(len(self.obstacles)):
            print(self.obstacles[i])
            x.append(self.obstacles[i][0])
            y.append(self.obstacles[i][1])
            z.append(self.obstacles[i][2])
            w.append(self.obstacles[i][3])
        
class RoombaCalculations():
    def __init__(self, master, room_x=150, room_y=150):
        self.master = master
        self.master.title("Roomba calculations")
        self.room = Canvas(self.master,
            width=room_x,
            height=room_y,
            bg="white"
        )
        self.room.pack()
        self.create_label("Ancho de la habitacion", 10, 10, 100, 20)
        self.create_label("Alto de la habitacion", 10, 30, 100, 20)
        self.create_label("Distancia del obstáculo con la pared derecha", 10, 50, 100, 20)
        self.create_label("Distancia del obstáculo con la pared superior", 10, 70, 100, 20)
        self.create_label("Ancho del cuadrado", 10, 90, 100, 20)
        self.create_label("Alto del cuadrado", 10, 110, 100, 20)
        self.create_label("Tiempo por metro cuadrado", 10, 130, 100, 20)
        e1 = self.create_entry(120, 10, 100, 20)
        e2 = self.create_entry(120, 30, 100, 20)
        e3 = self.create_entry(120, 50, 100, 20)
        e4 = self.create_entry(120, 70, 100, 20)
        e5 = self.create_entry(120, 90, 100, 20)
        e6 = self.create_entry(120, 110, 100, 20)
        e7 = self.create_entry(120, 130, 100, 20)
        self.create_button("Calcular", 10, 130, 100, 20, command=self.calculate(e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get()))
    #crea 1 boton para indicar el ancho y el alto del cuadrado

    def create_button(self, text, x, y, width, height, command):
        button = Button(self.master, text=text, command=command)
        button.place(x=x, y=y, width=width, height=height)
        return button
    
    def create_entry(self, x, y, width, height):
        entry = Entry(self.master)
        entry.place(x=x, y=y, width=width, height=height)
        return entry
    
    def create_label(self, text, x, y, width, height):
        label = Label(self.master, text=text)
        label.place(x=x, y=y, width=width, height=height)
        return label
    
    def calculate(self, max_width, max_height, distance_right, distance_top, square_width, square_height, tiempopormetrocuadrado=2):
        area1 = max_width * distance_top
        area2 = max_width * (max_height - distance_top - square_height)
        area3 = (max_width - distance_right - square_width) * max_height
        area4 = distance_right * max_height
        velocidad1 = area1 * tiempopormetrocuadrado
        velocidad2 = area2 * tiempopormetrocuadrado
        velocidad3 = area3 * tiempopormetrocuadrado
        velocidad4 = area4 * tiempopormetrocuadrado
        velocidadtotal = velocidad1 + velocidad2 + velocidad3 + velocidad4
        return velocidadtotal'''


'''if __name__ == "__main__":
    master = Tk()
    roomba = Roomba(master, 500, 690, 1)'''

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