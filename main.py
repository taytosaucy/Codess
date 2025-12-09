import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Ты гей?")
root.geometry("400x300")

def lol():
    messagebox.showinfo("Ты гей", "Ты гей")
def lolo():
    messagebox.showinfo("Не пизди, ты гей", "Не пизди, ты гей")

label = tk.Label(root, text="Ты гей?", font=30)
label.pack()

button1 = tk.Button(root, text="Да", command=lol, font=50)
button1.pack()
button1.place(x=140, y=25)

button2 = tk.Button(root, text="Нет",command=lolo, font=50)
button2.pack()
button2.place(x=230, y=25)

root.mainloop()