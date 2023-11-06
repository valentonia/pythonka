from tkinter import *

class IncomeWindow:
    def __init__(self):
        root = Tk()
        root.title("Income and Expenses")

        self.e = Entry(root, width = 35, borderwidth=5)
        self.e.grid(row = 0, column = 0, columnspan=1, padx = 10, pady = 10)

        self.b = Button(root, text = "Save", command=self.button_save)
        self.b.grid(row = 1, column = 0, padx=10)

        root.mainloop()
    
    def button_save(self):
        global income_l
                
        value = self.e.get()
        self.e.delete(0, END)
        
        old_value = income_l.cget("text")
        value = str(int(value) + int(old_value))
        
        income_l.config(text=value)
        
    def get_value(self):
        text = self.e.get()
        print(text)

class ExpenseWindow:
    def __init__(self):
        root = Tk()
        root.title("Income and Expenses")

        self.e = Entry(root, width = 35, borderwidth=5)
        self.e.grid(row = 0, column = 0, columnspan=3, padx = 10, pady = 10)
                
        button_1 = Button(root, text="1", padx=40, pady = 20, command=lambda:self.button_click(1))
        button_2 = Button(root, text="2", padx=40, pady = 20, command=lambda:self.button_click(2))
        button_3 = Button(root, text="3", padx=40, pady = 20, command=lambda:self.button_click(3))
        button_4 = Button(root, text="4", padx=40, pady = 20, command=lambda:self.button_click(4))
        button_5 = Button(root, text="5", padx=40, pady = 20, command=lambda:self.button_click(5))
        button_6 = Button(root, text="6", padx=40, pady = 20, command=lambda:self.button_click(6))
        button_7 = Button(root, text="7", padx=40, pady = 20, command=lambda:self.button_click(7))
        button_8 = Button(root, text="8", padx=40, pady = 20, command=lambda:self.button_click(8))
        button_9 = Button(root, text="9", padx=40, pady = 20, command=lambda:self.button_click(9))
        button_0 = Button(root, text="0", padx=40, pady = 20, command=lambda:self.button_click(0))
        button_add = Button(root, text="+", padx=39,pady=20,command=self.button_add)
        button_equal = Button(root, text="=", padx=91,pady=20,command=self.button_equal)
        button_save = Button(root, text="Save", padx=79,pady=20,command=self.button_save)

        button_1.grid(row=3, column = 0)
        button_2.grid(row=3, column = 1)
        button_3.grid(row=3, column = 2)

        button_4.grid(row=2, column = 0)
        button_5.grid(row=2, column = 1)
        button_6.grid(row=2, column = 2)

        button_7.grid(row=1, column = 0)
        button_8.grid(row=1, column = 1)
        button_9.grid(row=1, column = 2)

        button_0.grid(row=4, column = 0)
        button_save.grid(row=4, column=1,columnspan=2)
        button_add.grid(row=5, column=0)
        button_equal.grid(row=5,column=1,columnspan=2)
                
        root.mainloop()
        
    def button_click(self,number):
        current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0,str(current) + str(number))

    def button_save(self):
        global expense_l
                
        value = self.e.get()
        self.e.delete(0, END)
        
        old_value = expense_l.cget("text")
        value = str(int(value) + int(old_value))
        
        expense_l.config(text=value)
        
    def button_add(self):
        first_number = self.e.get()
        global f_num 
        f_num = int(first_number)
        self.e.delete(0, END)

    def button_equal(self):
        second_number = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, f_num + int(second_number))

root = Tk()
root.title("Income and Expense")

expense_b = Button(root, text = "Expense", command=ExpenseWindow)
income_b = Button(root, text = "Income", command=IncomeWindow)



expense_l = Label(root, text="0")
expense_l.grid(row=2)

income_l = Label(root, text="0")
income_l.grid(row=2, column=1)


expense_b.grid(row = 1, column = 0,padx = 15)
income_b.grid(row = 1, column = 1, padx = 15)
root.mainloop()