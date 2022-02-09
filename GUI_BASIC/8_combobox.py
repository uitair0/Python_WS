from cProfile import label
from tkinter import *
import tkinter
import tkinter.ttk as ttk

root = Tk()
root.title("Minsu Python Test")
root.geometry("640x480")

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

root.mainloop()
