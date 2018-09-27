import tkinter as tk


def btnHelloClicked():
    cd = float(entryCd.get())

    labelHello.config(text="%.2f mile = %.2f km" % (cd, cd * 1.60934))

top = tk.Tk()

top.title("Entry Test")

labelHello = tk.Label(top, text="Convert mile to km...", height=5, width=20, fg="blue")

labelHello.pack()

entryCd = tk.Entry(top, text="0")

entryCd.pack()

btnCal = tk.Button(top, text="Calculate", command=btnHelloClicked)

btnCal.pack()

top.mainloop()