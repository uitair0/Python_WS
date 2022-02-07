from tkinter import *
import tkinter

root = Tk()
root.title("Minsu Python Test")

btn1 = Button(root, text = "button1")
btn1.pack()
btn2 = Button(root, fg = "red", bg = "green", text = "button2")
btn2.pack()


root.mainloop()
