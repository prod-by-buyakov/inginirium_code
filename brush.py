import tkinter
import tkinter as tk
import time


def start_paint(event):
    global painted
    painted = True


def end_paint(event):
    global painted
    painted = False


def color_round(a):
    if len(hex(a)[2:]) < 2:
        return '0' + hex(a)[2:]
    else:
        return hex(a)[2:]


def change_color():
    global i, color
    r = i % 255
    g = 2 * i % 255
    b = 3 * i % 255
    color = "#" + color_round(r) + color_round(g) + color_round(b)
    canvas.itemconfig(oval, fill=color)

    if i == 255:
        i += 1
    else:
        i += 1
    root.after(5, change_color)


def sizeble(event):
    global size, oval
    if event.keysym == 'Up' and size <= 99:
        size += 1
    elif event.keysym == 'Down' and size > 0:
        size -= 1
    label.config(text=size)
    canvas.delete(oval)
    oval = canvas.create_oval(x - size, y - size, x + size, y + size, fill='#0f0')


def mouse_pos(ivent):
    global x, y
    x = ivent.x
    y = ivent.y
    canvas.moveto(oval, x - size, y - size)
    if painted:
        canvas.create_oval(x - size, y - size, x + size, y + size, outline=color, fill=color)


root = tk.Tk()
root.title('Brush')
color = '#0f0'
size = 5
x, y = 0, 0
i = 0
painted = False
label = tkinter.Label(root, text=size)
label.pack()
canvas = tkinter.Canvas(root, bg='#fff', width=640, height=640)
oval = canvas.create_oval(x - size, y - size, x + size, y + size, fill='#0f0')
canvas.pack()
change_color()
root.bind('<KeyPress>', sizeble)
root.bind('<Motion>', mouse_pos)
root.bind('<Button-1>', start_paint)
root.bind('<ButtonRelease-1>', end_paint)
root.mainloop()
