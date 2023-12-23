import tkinter
import tkinter as tk

def paint(event):
    canvas.create_oval(x-size,y-size,x+size,y+size,outline=color,fill=color)

def sizeble(event):
    global size,oval
    if event.keysym == 'Up' and size <=99:
        size += 1
    elif event.keysym == 'Down' and size >0:
        size -= 1
    label.config(text=size)
    canvas.delete(oval)
    oval = canvas.create_oval(x-size,y-size,x+size,y+size, fill='#0f0')
def mouse_pos(ivent):
    global x,y
    x = ivent.x
    y = ivent.y
    canvas.moveto(oval,x-size,y-size)

root = tk.Tk()
root.title('Brush')
color = '#0f0'
size = 5
x,y =0,0
label = tkinter.Label(root, text=size)
label.pack()
canvas = tkinter.Canvas(root, bg='#fff', width=640, height=640)
oval = canvas.create_oval(x-size,y-size,x+size,y+size, fill='#0f0')
canvas.pack()
root.bind('<KeyPress>', sizeble)
root.bind('<Motion>',mouse_pos)
root.bind('<Button-1>',paint)
root.mainloop()
