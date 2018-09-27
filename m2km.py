import tkinter as tk

def conventor():
    ent = float(btnentry.get())
    label.config(text="convert %.2f meter to %.2f kilometer" % (ent, ent/1000))

top = tk.Tk()

label = tk.Label(top, text="convent meter to kilometer....", fg="red")

label.pack()

btnentry = tk.Entry(top, text="0")

btnentry.pack()

btncal = tk.Button(top, text="press me", command=conventor)

btncal.pack()


top.mainloop()