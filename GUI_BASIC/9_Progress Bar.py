from cProfile import label
from tkinter import *
import tkinter
import tkinter.ttk as ttk
from unittest.mock import MagicMixin
import time

root = Tk()
root.title("Minsu Python Test")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar.start(10)  # move as 10ms
# progressbar.pack()

# def btncmd():
#     progressbar.stop()  # stop operation

# btn = Button(root, text="Selection", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(101):
        time.sleep(0.02)  # wait 0.01sec

        p_var2.set(i)  # set value of progress bar
        progressbar2.update()
        print(p_var2.get())


btn = Button(root, text="Start", command=btncmd2)
btn.pack()

root.mainloop()
