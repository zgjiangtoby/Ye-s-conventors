import tkinter as tk

def conventor():
    cd = float(entry.get())

    label.config(text="convert %.2f second to %.2f hour"%(cd, cd/3600))

top = tk.Tk()

label = tk.Label(top, text="convert second to hour...")
label.pack()

entry = tk.Entry(top, text="0")
entry.pack()

btn = tk.Button(top, text="Calculate", command=conventor)

btn.pack()

top.mainloop()