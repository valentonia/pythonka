from tkinter import *

def get_value():
    text = e.get()
    print(text)

root = Tk()
root.title("Income and Expenses")

e = Entry(root, width = 35, borderwidth=5)
e.grid(row = 0, column = 0, columnspan=1, padx = 10, pady = 10)

b = Button(root, text = "Save", command=get_value)
b.grid(row = 1, column = 0, padx=10)

root.mainloop()