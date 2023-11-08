import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

pastel_colors = ['#f0a3a3', '#FFCC99', '#99FF99', '#66B2FF', '#C2C2F0', '#FF99CC', '#99CCFF']

class IncomeExpenseTracker:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Income and Expenses")
        self.expenses = []
        
        # Create a button to show the pie chart
        self.pie_chart_button = tk.Button(self.root, text="Show Pie Chart", command=self.show_pie_chart)
        self.pie_chart_button.grid(row=7, column=1)

        # Income Entry
        self.income_label = tk.Label(self.root, text="Income:")
        self.income_label.grid(row=0, column=0)
        self.income_entry = tk.Entry(self.root, width=15, borderwidth=5)
        self.income_entry.grid(row=0, column=1, padx=10, pady=10)
        self.income_button = tk.Button(self.root, text="Save Income", command=self.save_income)
        self.income_button.grid(row=0, column=2)

        # Expense Category Combobox
        self.expense_category_label = tk.Label(self.root, text="Select Category:")
        self.expense_category_label.grid(row=2, column=0)
        self.expense_categories = ['Fashion', 'Traveling', 'Food', 'Hospitality', 'Utility bills','Selfcare','Emergency']
        self.selected_category = tk.StringVar()
        self.expense_category_combobox = ttk.Combobox(self.root, textvariable=self.selected_category, values=self.expense_categories)
        self.expense_category_combobox.grid(row=2, column=1, padx=10, pady=10)

        # Expense Amount Entry
        self.expense_amount_label = tk.Label(self.root, text="Expense Amount:")
        self.expense_amount_label.grid(row=3, column=0)
        self.expense_amount_entry = tk.Entry(self.root, width=15, borderwidth=5)
        self.expense_amount_entry.grid(row=3, column=1, padx=10, pady=10)

        # Save Expense Category Button
        self.save_expense_category_button = tk.Button(self.root, text="Save Expense Category", command=self.save_expense_category)
        self.save_expense_category_button.grid(row=3, column=2)

        # Track Total Income and Expenses
        self.income_total_label = tk.Label(self.root, text="Total Income:")
        self.income_total_label.grid(row=5, column=0)
        self.income_total = 0
        self.income_total_display = tk.Label(self.root, text=str(self.income_total))
        self.income_total_display.grid(row=5, column=1)

        self.expense_total_label = tk.Label(self.root, text="Total Expenses:")
        self.expense_total_label.grid(row=6, column=0)
        self.expense_total = 0
        self.expense_total_display = tk.Label(self.root, text=str(self.expense_total))
        self.expense_total_display.grid(row=6, column=1)

    def save_income(self):
        income = self.income_entry.get()
        try:
            income = float(income)
            self.income_total += income
            self.income_total_display.config(text=str(self.income_total))
            self.income_entry.delete(0, tk.END)
        except ValueError:
            pass

    def save_expense_category(self):
        category = self.selected_category.get()
        amount = self.expense_amount_entry.get()
        try:
            amount = float(amount)
            self.expense_total += amount
            self.expense_total_display.config(text=str(self.expense_total))
            self.expense_amount_entry.delete(0, tk.END)
            self.expenses.append(Expense(category, amount))  # Add the expense object to the list
        except ValueError:
            pass

    def show_pie_chart(self):
        category_expenses = {}
        pastel_palette = random.sample(pastel_colors, len(self.expense_categories))

        for expense in self.expenses:
            category = expense.category
            amount = expense.amount

            if category not in category_expenses:
                category_expenses[category] = 0

            category_expenses[category] += amount

        if category_expenses:
            fig = Figure(figsize=(6, 6))
            ax = fig.add_subplot(111)

            labels = category_expenses.keys()
            sizes = category_expenses.values()

            # Use pastel colors for the pie chart
            colors = pastel_palette[:len(labels)]

            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
            ax.set_title('Expense Categories')

            pie_chart = FigureCanvasTkAgg(fig, self.root)
            pie_chart.get_tk_widget().grid(row=8, column=1)
            pie_chart.draw()

class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

if __name__ == "__main__":
    root = tk.Tk()
    app = IncomeExpenseTracker(root)
    root.mainloop()