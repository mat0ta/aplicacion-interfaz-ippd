from tkinter import *
from threading import *
from time import sleep

class Roomba():
    def __init__(self, master, room_x=100, room_y=100, obstacles_number=0):
        self.master = master
        self.master.title("Roomba")
        self.room = Canvas(self.master,
            width=room_x,
            height=room_y,
            bg="white"
        )
        self.master.bind('<Escape>', lambda e: self.master.quit())

        self.cleaned = []
        self.obstacles = [[]]
        for i in range(obstacles_number):    
            x = int(input("Introduce la distancia entre el Objeto " + str(i) + " y la pared derecha: "))
            y = int(input("Introduce la distancia entre el Objeto " + str(i) + " y la pared superior: "))
            self.room.create_rectangle(x, y, room_x - x, room_y - y, fill="green")
            self.obstacles[i] = [x, y, room_x - x, room_y - y]
        self.roomba = self.room.create_oval(1, 1, 10, 10, fill="red")
        self.actual_x = 1
        self.actual_y = 1
        self.master.update()
        self.room.update()
        self.room.pack()
        while True:
            self.initiate()
            mainloop()
    
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
    def __init__(self, room_x=100, room_y=100, obstacles = []):
        self.room_x = room_x
        self.room_y = room_y
        self.obstacles = obstacles
        self.sections = []
    
    def calculate(self):
        for i in self.obstacles:
            section_1 = [0]

if __name__ == "__main__":
    master = Tk()
    roomba = Roomba(master, 500, 690, 1)