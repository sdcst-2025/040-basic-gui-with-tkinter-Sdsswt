import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Example")
window.geometry("260x135")

dogphoto = PhotoImage(file="dog.png")
photo = tk.Label(window, image=dogphoto)
photo.grid(row = 1, column = 2)


title = tk.Label(window, text="Pachacco!",)
title.grid(row=1, column=2,sticky="E")

label1 = tk.Label(window, text="A cuddly little puppy! This is from the same \n creators who brought you keropi and kero kero",bg="#aaffff")
label1.grid(row=4, column=2)



window.mainloop()