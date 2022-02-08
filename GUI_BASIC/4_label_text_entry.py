from cProfile import label
from cgitb import text
from tkinter import *
import tkinter

root = Tk()
root.title("Minsu Python Test")
root.geometry("640x480")

label1 = Label(root, text="hello world")
label1.pack()


def changeText():
    label1.config(text="good bye!!")


btn1 = Button(root, command=changeText, text="Click!!")
btn1.pack()

txt = Text(root, width=30, height=5)  # more than one line
txt.pack()

txt.insert(END, "write something")

e = Entry(root, width=30)  # one line
e.pack()
e.insert(0, "only one row available")


def btncmd():
    print(txt.get("1.0", END))  # 1: 1st line 0: 0th column
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)


btn2 = Button(root, text="click", command=btncmd)
btn2.pack()

root.mainloop()
