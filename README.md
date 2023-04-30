# Aplicacion-interfaz-ippd

En este [repositorio](https://github.com/mat0ta/aplicacion-interfaz-ippd) queda el código del rumba y la interfaz gráfica.

<h2>¡Creando una interfaz gráfica!</h2>

Lo primero que hemos hecho para sacar nuestra interfaz gráfica siguiendo la guía del aula virtual es crear un entorno virtual. Para ello abrimos la terminal:

![capt1](https://user-images.githubusercontent.com/91721699/219425517-3101e24c-eb45-4ec9-abb1-9b47221ef573.png)

y comenzamos comprobando la version actual de python.

![capt2](https://user-images.githubusercontent.com/91721699/219425584-6ca52845-6c83-4b70-ae19-2a294d671ba2.png)

Tras ello, ejecutamos la siguiente linea de código:

![capt3](https://user-images.githubusercontent.com/91721699/219425646-c1687520-029c-45bd-94f0-f3c966be5c98.png)

que crea nuestra carpeta entorno1 con su propio etorno virtual en el que poder importar las librerias necesarias para nuestro proyecto.

![capt4](https://user-images.githubusercontent.com/91721699/219425702-e687bfbf-410b-46a6-a1d2-fd3206a9a327.png)

Como se puede observar en la imagen anterior, nuestro nuevo entorno contiene todas las carpetas necesarias como bin y scripts.
Tras terminar de configurar nuestro entorno, procedemos a asegurarnos de tener la última versión posible de pip utilizando el comando --upgrade pip.

![capt5](https://user-images.githubusercontent.com/91721699/219425728-2fa387d8-4cf3-46de-a402-4effb505d52a.png)

Para proseguir, hemos recreado y corregido las lecciones del aula Multihilo e IHM:

<h3>Código Multihilo</h3>

```python
import threading 
import time 
 
class Rodar(threading.Thread): 
    def __init__(self): 
        super().__init__() 
 
    def run(self): 
        # El bloqueo es capturado por el thread. 
        # Todos los demás threads que quieran capturar este bloqueo 
        # esperarán hasta que se libere. 
        bloqueo.acquire() 
        for _ in range(5): 
            print('.', end='') 
            time.sleep(.2) 
        # Liberación del bloqueo. Entre los otros threads que 
        # estaban esperando capturarlo, solo se seleccionará uno 
        # por el sistema operativo para recuperarlo. 
        bloqueo.release() 
 
class Girar(threading.Thread): 
    def __init__(self): 
        super().__init__() 
 
    def run(self): 
        bloqueo.acquire() 
        for _ in range(3): 
            print('->', end='') 
            time.sleep(.2) 
        bloqueo.release() 

class Coche(): 
    def __init__(self): 
        # Instancia de la clase de acción para rodar. 
        self.rodar = Rodar() 
        # Instancia de la clase de acción para girar. 
        self.girar = Girar() 
 
    # Durante el arranque, se quiere rodar y girar simultáneamente. 
    def arrancar(self): 
        # El método start() oculta la mecánica de lanzamiento del 
        # thread y su asociación con el proceso padre, y 
        # una vez que el thread ha comenzado, llama a su método run() 
        # que realizará la tarea paralela. 
        self.rodar.start() 
        self.girar.start() 
 
# Coche inalterado. 
 
# Declaración del bloqueo, recurso común entre los dos threads. 
bloqueo = threading.Lock() 
coche = Coche() 
coche.arrancar()
```
El output:

![capt6](https://user-images.githubusercontent.com/91721699/219425768-124e5335-0b28-4ac8-96b6-326a78b0b069.png)

<h3>Código IHM: Tkinter</h3>

```python
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

```
El output:

![capt7](https://user-images.githubusercontent.com/91721699/219425890-ae15e5c6-6e6b-4959-b9bf-fc2fa01dbeda.png)

![capt8](https://user-images.githubusercontent.com/91721699/219425911-9365184c-5d12-45e4-92a8-247cf038e56c.png)

![capt9](https://user-images.githubusercontent.com/91721699/219425935-d034eaba-6364-4e1a-b333-a571e3f83202.png)

<h3>Código IHM: QT</h3>

```python
# No olvidar importar las clases necesarias. 
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QSpinBox, QLineEdit, QHBoxLayout, QComboBox 
import sys
 
# Definición de una QMainWindow personalizada para poder 
# crear instancias de futuros widgets en ella. 
class MainWindow(QMainWindow): 
    def __init__(self): 
        super(MainWindow, self).__init__()


class MainWindow2(QMainWindow): 
    def __init__(self): 
        super(MainWindow2, self).__init__() 
 
        # Widget básico que sirve como base para la jerarquía 
        # de los sub-widgets. 
        widget = QWidget() 
 
        # Especifica que el widget principal de la ventana es 
        # el widget que se acaba de instanciar. 
        self.setCentralWidget(widget) 
 
        # Nueva distribución horizontal. 
        diseño = QHBoxLayout() 
        # Asignación del diseño horizontal 
        # al widget principal. 
        widget.setLayout(diseño) 
 
        # Los operandos se representan por spinboxes. 
        self.operando1 = QSpinBox() 
        self.operando2 = QSpinBox() 
 
        # Un menú desplegable le permite elegir la operación 
        # que se debe aplicar. Primero tiene que instanciarla. 
        self.operacion = QComboBox() 
        # Luego, insertamos los símbolos en el menú para 
        # poder seleccionarlos más tarde. 
        [self.operacion.addItem(op) for op in ["+", "-", "*", "/"]] 
 
        # Finalmente, el resultado de la operación está representado 
        # por una zona de texto. 
        self.resultado = QLineEdit() 
 
        # Uso de un generador para agregar fácilmente 
        # los widgets al layout. 
        widgets = [self.operando1, self.operacion, self.operando2, 
                   QLabel("="), self.resultado] 
        [diseño.addWidget(widget) for widget in widgets] 



class MainWindow3(QMainWindow): 
    def __init__(self): 
        super(MainWindow3, self).__init__() 
 
        # Widget básico que sirve como base para la jerarquía 
        # de los sub-widgets. 
        widget = QWidget() 
 
        # Especifica que el widget principal de la ventana es 
        # el widget que se acaba de instanciar. 
        self.setCentralWidget(widget) 
 
        # Nueva distribución horizontal. 
        diseño = QHBoxLayout() 
        # Asignación del diseño horizontal 
        # al widget principal. 
        widget.setLayout(diseño) 
 
        # Los operandos se representan por spinboxes. 
        self.operando1 = QSpinBox() 
        self.operando2 = QSpinBox() 
 
        # Un menú desplegable le permite elegir la operación 
        # que se debe aplicar. Primero tiene que instanciarla. 
        self.operacion = QComboBox() 
        # Luego, insertamos los símbolos en el menú para 
        # poder seleccionarlos más tarde. 
        [self.operacion.addItem(op) for op in ["+", "-", "*", "/"]] 
 
        # Finalmente, el resultado de la operación está representado 
        # por una zona de texto. 
        self.resultado = QLineEdit() 
 
        # Uso de un generador para agregar fácilmente 
        # los widgets al layout. 
        widgets = [self.operando1, self.operacion, self.operando2, 
                   QLabel("="), self.resultado] 
        [diseño.addWidget(widget) for widget in widgets]

         # La clase QSpinBox emite una señal valueChanged(int) 
        # cuando se modifica el valor mostrado en el spinbox. 
        # Conectamos esta señal al slot calcular(), que es un 
        # método de la clase MainWindow. Los prototipos son 
        # diferentes, pero el hecho de perder el parámetro de 
        # la señal, es irrelevante porque el slot puede recuperar 
        # el nuevo valor accediendo directamente a la spinbox. 
        self.operando1.valueChanged.connect(self.calcular) 
        self.operando2.valueChanged.connect(self.calcular) 
 
        # La clase QComboBox emite una señal 
        # currentTextChanged(QString) cuando el usuario ha 
        # seleccionado un nuevo valor del menú desplegable. 
        # Conectamos esta señal al slot calcular(). Aquí también, 
        # el nuevo texto del menú desplegable que lleva la 
        # señal, se puede ignorar. 
        self.operacion.currentIndexChanged.connect(self.calcular) 
 
        # Para que el widget que muestra el resultado esté actualizado 
        # tan pronto como se realiza la construcción de la ventana, 
        # realizamos el cálculo desde el constructor. 
        self.calcular()

    def calcular(self): 
        # Primer operando. 
        a = self.operando1.value() 
        # Segundo operando. 
        b = self.operando2.value() 
 
        # Realizamos la operación correspondiente al texto 
        # seleccionado en el menú desplegable y transformamos 
        # el resultado en cadena de caracteres gracias a la 
        # función str (). 
        if (self.operacion.currentText() == "+"): 
            resultado = str(a + b) 
        elif (self.operacion.currentText() == "-"): 
            resultado = str(a - b) 
        elif (self.operacion.currentText() == "*"): 
            resultado = str(a * b) 
        elif (self.operacion.currentText() == "/"): 
            # Atención a la división por cero 
            try: 
                resultado = str(a / b) 
            except ZeroDivisionError as e: 
                resultado = "División por cero" 
        # Cambiamos el campo texto con el resultado de la operación. 
        self.resultado.setText(resultado)


if __name__ == '__main__':
 
    # QApplication requiere la lista de argumentos pasadas 
    # al ejecutable durante su instanciación. 
    app = QApplication(sys.argv) 
 
    # Creación de la ventana principal. 
    window = MainWindow3() 
 
    # Visualización de la ventana principal. 
    window.show() 
 
    # Inicio del bucle de eventos, cuyo valor 
    # de retorno se utilizará como código de salida de la ejecución. 
    sys.exit(app.exec_())
   
```

El output:

![capt10](https://user-images.githubusercontent.com/91721699/219425996-abd8fac0-9ac8-45ef-a6e5-3bc92685c7b8.png)

<h2>¡Roomba!</h2>

Nuestro roomba primero crea una interfaz gráfica que te permite introducir los datos de la habitación a limpiar además de los del obstáculo que el aparato deberá evitar.

![capt12](https://user-images.githubusercontent.com/91721699/235369915-20d3d439-ad1e-4333-9c58-8634b02dc352.png)

Luego crea a partir de esos datos una representación de la habitación en otra ventana y finalmente desvela el tiempo que tarda en limpiarse cada zona junto con el tiempo total.

![capt11](https://user-images.githubusercontent.com/91721699/235370031-ea51270e-2fea-439f-91d9-4cc140ed5117.png)

![capt13](https://user-images.githubusercontent.com/91721699/235370037-1cf363cb-b4bc-4a25-bc49-cce38efc72d9.png)

El código con el que se ha construido esta GUI es:

```py
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
```
