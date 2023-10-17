
import tkinter as tk

window = tk.Tk()

frame_income_expense = tk.Frame()
frame_income_expense.pack()
label_expense = tk.Label(text="Expense", master=frame_income_expense)
label_expense.grid(row=0, column=0, sticky="ew", padx=5)
label_income = tk.Label(text="Income", master=frame_income_expense)
label_income.grid(row=0, column=1, sticky="ew", padx=5)

frame_2 = tk.Frame()
frame_2.pack()
label_expense_n = tk.Label(text="0.00", master=frame_2)
label_expense_n.grid(row=0, column=0, sticky="e")
label_income_n = tk.Label(text="0.00", master=frame_2)
label_income_n.grid(row=0, column=1, sticky="")

#file = open()
#l = 

window.mainloop()
