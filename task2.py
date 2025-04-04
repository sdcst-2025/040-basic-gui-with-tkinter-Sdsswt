import tkinter as tk


window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("700x300")


search = tk.Label(window, text="Search by Name")
search.grid(row=0, column=2, sticky="e", padx=5, pady=5)

search = tk.Entry(window, width=20)
search.grid(row=0, column=3, padx=5, pady=5)


title = tk.Label(window, text="Client Database")
title.grid(row=1, column=1, columnspan=3, pady=5)


name = tk.Label(window, text="Name")
name.grid(row=2, column=0, padx=5)

type = tk.Label(window, text="Type")
type.grid(row=2, column=1, padx=5)

breed = tk.Label(window, text="Breed")
breed.grid(row=2, column=2, padx=5)

owner = tk.Label(window, text="Owner")
owner.grid(row=2, column=3, padx=5)

birthdate = tk.Label(window, text="Birthdate")
birthdate.grid(row=2, column=4, padx=5)


name = tk.Entry(window, width=15)
name.grid(row=3, column=0)

type = tk.Entry(window, width=15)
type.grid(row=3, column=1)

breed = tk.Entry(window, width=15)
breed.grid(row=3, column=2)

owner = tk.Entry(window, width=15)
owner.grid(row=3, column=3)

birthdate = tk.Entry(window, width=15)
birthdate.grid(row=3, column=4)


prev_button = tk.Button(window, text="< Previous")
prev_button.grid(row=4, column=0)

save_button = tk.Button(window, text="Save Entry")
save_button.grid(row=4, column=2)

next_button = tk.Button(window, text="Next >")
next_button.grid(row=4, column=4)


window.mainloop()