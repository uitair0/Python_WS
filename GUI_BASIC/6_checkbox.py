from tkinter import *
import tkinter

root = Tk()
root.title("Minsu Python Test")
root.geometry("640x480")

chkvar = IntVar()
chkbox = Checkbutton(root, text="do not open today!!", variable=chkvar)
# chkbox.select()
# chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="do not open in this week", variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get())
    print(chkvar2.get())


btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
