import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("700x300")

dogphoto = PhotoImage(file="dog.png")
photo = tk.Label(window, image=dogphoto)
photo.grid(row = 0, column = 0)

search = tk.Label(window, text="Search by Name")
search.grid(row=3, column=2,)

search = tk.Entry(window, width=20)
search.grid(row=3, column=3)

title = tk.Label(window, text="Client Database")
title.grid(row=4, column=1)

name = tk.Label(window, text="Name")
name.grid(row=5, column=0)

type = tk.Label(window, text="Type")
type.grid(row=5, column=1)

breed = tk.Label(window, text="Breed")
breed.grid(row=5, column=2)

owner = tk.Label(window, text="Owner")
owner.grid(row=5, column=3)

birthdate = tk.Label(window, text="Birthdate")
birthdate.grid(row=5, column=4)

name = tk.Entry(window, width=15)
name.grid(row=6, column=0)

type = tk.Entry(window, width=15)
type.grid(row=6, column=1)

breed = tk.Entry(window, width=15)
breed.grid(row=6, column=2)

owner = tk.Entry(window, width=15)
owner.grid(row=6, column=3)

birthdate = tk.Entry(window, width=15)
birthdate.grid(row=6, column=4)

prev_button = tk.Button(window, text="< Previous")
prev_button.grid(row=7, column=0)

save_button = tk.Button(window, text="Save Entry")
save_button.grid(row=7, column=2)

next_button = tk.Button(window, text="Next >")
next_button.grid(row=7, column=4)

window.mainloop()