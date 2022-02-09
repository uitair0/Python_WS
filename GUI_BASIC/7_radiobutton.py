from cProfile import label
from tkinter import *
import tkinter

root = Tk()
root.title("Minsu Python Test")
root.geometry("640x480")

Label(root, text="select menu").pack()
burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="Hamburger", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="Cheeseburger",
                          value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="Chickenburger",
                          value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="select drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="coke", value="coke", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="cydar", value="cydar", variable=drink_var)
btn_drink3 = Radiobutton(root, text="lemonade",
                         value="lemonade", variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()


def btncmd():
    print(burger_var.get())
    print(drink_var.get())


btn = Button(root, text="Order", command=btncmd)
btn.pack()

root.mainloop()
