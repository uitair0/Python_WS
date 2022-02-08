from cProfile import label
from cgitb import text
from tkinter import *
import tkinter

root = Tk()
root.title("Minsu Python Test")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)  # extended, single
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermallon")
listbox.insert(END, "graph")
listbox.pack()


def btncmd():
    # listbox.delete(END)  # END: delete last item, 0:1st item
    #print("list has", listbox.size(), "ea.")
    #print("1st ~ 3th item : ", listbox.get(0, 2))
    print("selected item : ", listbox.curselection())  # return the index


btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
