from distutils.command.build import build
from tkinter import *
import tkinter

root = Tk()
root.title("Minsu Dialog")

btn1 = Button(root, text="button1")
btn1.pack()
btn2 = Button(root,  padx=50, pady=10, text="button2")
btn2.pack()
# padx and pady impact to out of width/height of button
btn3 = Button(root, text="button3", padx=15, pady=10)
btn3.pack()
btn4 = Button(root, width=10, height=5, text="button4")
btn4.pack()
btn5 = Button(root, fg="green", bg="black", text="button5")
btn5.pack()

img1 = tkinter.PhotoImage(file="icon2.png")
btn6 = Button(root, image=img1)
btn6.pack()


def clickEvent():
    print("clicked button")


btn7 = Button(root, command=clickEvent, text="button7")
btn7.pack()

root.mainloop()
