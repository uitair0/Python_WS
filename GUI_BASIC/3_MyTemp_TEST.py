from tkinter import *
import tkinter

root = Tk()
root.title("Minsu Python Test")

btn1 = Button(root, text="button1")
btn1.pack()
btn2 = Button(root, fg="red", bg="green", text="button2")
btn2.pack()

img1 = PhotoImage(file="icon.png")

btn3 = Button(root, image=img1)
btn3.pack()


def clickEvent():
    print("Button is clicked!!")


btn4 = Button(root, command=clickEvent, text="Click!!")
btn4.pack()

root.mainloop()
