import tkinter as tk 
from tkinter import *


window = tk.Tk()
window.title("tk")
window.geometry("500x50")

frame = Frame(window)
frame.pack()

bottomframe = Frame(window)
bottomframe.pack( side = BOTTOM )

box1 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
box1.pack(side = LEFT)

x_label = tk.Button(window,text="x")
x_label.pack(side = LEFT)

box2 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
box2.pack(side = LEFT )

x_label = tk.Button(window,text="=")
x_label.pack(side = LEFT)

box3 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
box3.pack(side = LEFT )

window.mainloop()