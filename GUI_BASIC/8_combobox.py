from cProfile import label
from tkinter import *
import tkinter
import tkinter.ttk as ttk


from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


root = Tk()
root.title("Minsu Python Test")
root.geometry("640x480")

fig = Figure(figsize=(5, 4), dpi=100)
# t = np.arange(0, 3, .01)
# fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
ax = fig.add_subplot(1,1,1)

matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'Javascript', 'C++', 'C#', 'ETC']
plt.pie(values, labels=labels, autopct='%.1f%%',
        startangle=90, counterclock=False)
ax.pie(values, labels=labels, autopct='%.1f%%',
        startangle=90, counterclock=False)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

values = [str(i) + "day" for i in range(1, 32)]  # 1 ~ 31
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("Select day")

readonly_combobox = ttk.Combobox(
    root, height=10, values=values, state="readonly")
readonly_combobox.current(0)
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())


btn = Button(root, text="Order", command=btncmd)
btn.pack()

canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


root.mainloop()
