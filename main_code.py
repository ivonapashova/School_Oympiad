import tkinter as tk

def start_drag(event):
    element_label = event.widget
    element_label.data = {'x': event.x, 'y': event.y}

def stop_drag(event):
    element_label = event.widget
    del element_label.data

def on_drag(event):
    element_label = event.widget
    x, y = event.x, event.y
    x_delta = x - element_label.data['x']
    y_delta = y - element_label.data['y']
    element_label.place(x=element_label.winfo_x() + x_delta, y=element_label.winfo_y() + y_delta)
    element_label.data['x'] = x
    element_label.data['y'] = y

root = tk.Tk()
root.title("Симулация на запояване")

# платката-фон
board_image = tk.PhotoImage(file="board.png")
board_label = tk.Label(root, image=board_image)
board_label.place(x=0, y=0)

element1_image = tk.PhotoImage(file="резистор.png")
element1_image = element1_image.subsample(3, 3)  # Умалено изображение
element2_image = tk.PhotoImage(file="kondenzator.webp")
element2_image = element2_image.subsample(3, 3)  # Умалено изображение
element3_image = tk.PhotoImage(file="diod.png")
element3_image = element3_image.subsample(3, 3)  # Умалено изображение

element1_label = tk.Label(root, image=element1_image)
element2_label = tk.Label(root, image=element2_image)
element3_label = tk.Label(root, image=element3_image)

element1_label.place(x=50, y=50)
element2_label.place(x=50, y=280)
element3_label.place(x=50, y=550)

# за всеки елемент
element1_label.bind("<Button-1>", start_drag)
element1_label.bind("<ButtonRelease-1>", stop_drag)
element1_label.bind("<B1-Motion>", on_drag)

element2_label.bind("<Button-1>", start_drag)
element2_label.bind("<ButtonRelease-1>", stop_drag)
element2_label.bind("<B1-Motion>", on_drag)

element3_label.bind("<Button-1>", start_drag)
element3_label.bind("<ButtonRelease-1>", stop_drag)
element3_label.bind("<B1-Motion>", on_drag)

root.geometry("800x600")
root.mainloop()
