import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Example")
window.geometry("260x135")

dogphoto = PhotoImage(file="dog.png")
photo = tk.Label(window, image=dogphoto)
photo.place(x=1, y=1)


title = tk.Label(window, text="Pachacco!",)
title.place(x=75,y=50)

label1 = tk.Label(window, text="A cuddly little puppy! This is from the same \n creators who brought you keropi and kero kero",bg="#aaffff")
label1.place(x=1,y=100)



window.mainloop()