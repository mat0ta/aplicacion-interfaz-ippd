import tkinter as tk

def calculate_time(x1_slider, y1_slider, x2_slider, y2_slider, result_label):
    width = int(width_entry.get())
    length = int(length_entry.get())
    x1 = int(x1_slider.get())
    y1 = int(y1_slider.get())
    x2 = int(x2_slider.get())
    y2 = int(y2_slider.get())

    room_area = width * length

    obstacle_area = abs(x2 - x1) * abs(y2 - y1)

    cleanable_area = room_area - obstacle_area

    cleaning_time = cleanable_area / 10

    result_label.config(text=f"Cleaning time: {cleaning_time} minutes")

def obstacle_window():
    max_x = int(width_entry.get())
    max_y = int(length_entry.get())

    obstacle_window = tk.Tk()

    x1_label = tk.Label(root, text="Obstacle x1:")
    x1_label.grid(row=2, column=0)
    x1_slider = tk.Scale(root, from_=0, to=max_x, orient=tk.HORIZONTAL)
    x1_slider.grid(row=2, column=1)

    y1_label = tk.Label(root, text="Obstacle y1:")
    y1_label.grid(row=3, column=0)
    y1_slider = tk.Scale(root, from_=0, to=max_y, orient=tk.HORIZONTAL)
    y1_slider.grid(row=3, column=1)

    x2_label = tk.Label(root, text="Obstacle x2:")
    x2_label.grid(row=4, column=0)
    x2_slider = tk.Scale(root, from_=0, to=max_x, orient=tk.HORIZONTAL)
    x2_slider.grid(row=4, column=1)

    y2_label = tk.Label(root, text="Obstacle y2:")
    y2_label.grid(row=5, column=0)
    y2_slider = tk.Scale(root, from_=0, to=max_y, orient=tk.HORIZONTAL)
    y2_slider.grid(row=5, column=1)

    calculate_button = tk.Button(root, text="Calculate", command=calculate_time(x1_slider, y1_slider, x2_slider, y2_slider, result_label))
    calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

    result_label = tk.Label(root, text="")
    result_label.grid(row=7, column=0, columnspan=3)

    obstacle_window.mainloop()


root = tk.Tk()
root.title("Roomba Cleaning Time Calculator")

width_label = tk.Label(root, text="Room width (ft):")
width_label.grid(row=0, column=0)
width_entry = tk.Entry(root)
width_entry.grid(row=0, column=1)

length_label = tk.Label(root, text="Room length (ft):")
length_label.grid(row=1, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1)

# x1_label = tk.Label(root, text="Obstacle x1:")
# x1_label.grid(row=2, column=0)
# x1_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
# x1_slider.grid(row=2, column=1)

# y1_label = tk.Label(root, text="Obstacle y1:")
# y1_label.grid(row=3, column=0)
# y1_entry = tk.Entry(root)
# y1_entry.grid(row=3, column=1)

# x2_label = tk.Label(root, text="Obstacle x2:")
# x2_label.grid(row=4, column=0)
# x2_entry = tk.Entry(root)
# x2_entry.grid(row=4, column=1)

# y2_label = tk.Label(root, text="Obstacle y2:")
# y2_label.grid(row=5, column=0)
# y2_entry = tk.Entry(root)
# y2_entry.grid(row=5, column=1)

# calculate_button = tk.Button(root, text="Calculate", command=calculate_time)
# calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

next_button = tk.Button(root, text="Next", command=lambda: [obstacle_window(), root.destroy()])
next_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()