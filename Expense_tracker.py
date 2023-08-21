import tkinter as tk
from tkinter import messagebox, filedialog

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expenses Tracker")
        
        self.expenses = []
        self.descriptions = []
        
        self.create_ui()
        
    def create_ui(self):
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.create_expense_list()
        self.create_total_label()
        
    def create_labels(self):
        self.label_description = tk.Label(self.root, text="Expense Description:")
        self.label_description.pack()
        
        self.label_amount = tk.Label(self.root, text="Expense Amount:")
        self.label_amount.pack()
        
    def create_entries(self):
        self.entry_description = tk.Entry(self.root)
        self.entry_description.pack()
        
        self.entry_amount = tk.Entry(self.root)
        self.entry_amount.pack()
        
    def create_buttons(self):
        self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_button.pack()
        
        self.edit_button = tk.Button(self.root, text="Edit Expense", command=self.edit_selected_expense)
        self.edit_button.pack()
        
        self.save_button = tk.Button(self.root, text="Save Expenses", command=self.save_expenses)
        self.save_button.pack()
        
        self.load_button = tk.Button(self.root, text="Load Expenses", command=self.load_expenses)
        self.load_button.pack()
        
        self.report_button = tk.Button(self.root, text="Generate Expense Report", command=self.generate_report)
        self.report_button.pack()
        
    def create_expense_list(self):
        self.expense_list = tk.Listbox(self.root)
        self.expense_list.pack()
        
    def create_total_label(self):
        self.total_label = tk.Label(self.root, text="Total Expenses: ₹0")
        self.total_label.pack()
        
    def add_expense(self):
        description = self.entry_description.get()
        amount = self.entry_amount.get()
        
        if description and amount:
            self.descriptions.append(description)
            self.expenses.append(float(amount))
            self.update_expense_list()
            self.update_total_label()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please enter a valid description and amount.")
        
    def update_expense_list(self):
        self.expense_list.delete(0, tk.END)
        for description, amount in zip(self.descriptions, self.expenses):
            self.expense_list.insert(tk.END, f"Expense: {description} - ₹{amount:.2f}")
        
    def update_total_label(self):
        total = sum(self.expenses)
        self.total_label.config(text=f"Total Expenses: ₹{total:.2f}")
        
    def clear_entries(self):
        self.entry_description.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)
        
    def save_expenses(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                for description, amount in zip(self.descriptions, self.expenses):
                    file.write(f"{description},{amount}\n")
            messagebox.showinfo("Info", "Expenses saved successfully.")
            
    def load_expenses(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.expenses = []
            self.descriptions = []
            with open(file_path, "r") as file:
                for line in file:
                    description, amount = line.strip().split(",")
                    self.descriptions.append(description)
                    self.expenses.append(float(amount))
            self.update_expense_list()
            self.update_total_label()
            messagebox.showinfo("Info", "Expenses loaded successfully.")
            
    def generate_report(self):
        total = sum(self.expenses)
        report = f"Expense Report\nTotal Expenses: ₹{total:.2f}\n\n"
        for description, amount in zip(self.descriptions, self.expenses):
            report += f"Expense: {description} - ₹{amount:.2f}\n"
        report_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if report_path:
            with open(report_path, "w", encoding="utf-8") as file:  # Specify the encoding as utf-8
                file.write(report)
            messagebox.showinfo("Info", "Expense report generated successfully.")
    
    def edit_selected_expense(self):
        selected_indices = self.expense_list.curselection()
        if selected_indices:
            selected_index = selected_indices[0]
            selected_description, selected_amount = self.descriptions[selected_index], self.expenses[selected_index]
            self.entry_description.delete(0, tk.END)
            self.entry_amount.delete(0, tk.END)
            self.entry_description.insert(0, selected_description)
            self.entry_amount.insert(0, selected_amount)
            self.delete_selected_expense(selected_index)

    def delete_selected_expense(self, index):
        del self.descriptions[index]
        del self.expenses[index]
        self.update_expense_list()
        self.update_total_label()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.geometry("300x400")
    root.mainloop()
