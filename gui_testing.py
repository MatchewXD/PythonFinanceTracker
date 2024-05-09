import tkinter as tk
from tkinter import ttk

def add_transaction():
    # Retrieve data from entries
    data = (entry_date.get(), entry_amount.get(), entry_category.get(), entry_store.get())
    # Insert data into the Treeview
    tree.insert('', tk.END, values=data)
    # Clear the entries for new data input
    entry_date.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_store.delete(0, tk.END)

# Setup the main window
window = tk.Tk()
window.title("Financial Tracker")
window.geometry("600x400")

# Entry widgets for each field
entry_date = tk.Entry(window, width=10)
entry_date.pack(side=tk.LEFT, padx=(10, 2), pady=10)
entry_amount = tk.Entry(window, width=10)
entry_amount.pack(side=tk.LEFT, padx=2, pady=10)
entry_category = tk.Entry(window, width=15)
entry_category.pack(side=tk.LEFT, padx=2, pady=10)
entry_store = tk.Entry(window, width=15)
entry_store.pack(side=tk.LEFT, padx=2, pady=10)

# Button to add a transaction
add_button = tk.Button(window, text="Add Transaction", command=add_transaction)
add_button.pack(pady=10)

# Treeview widget setup
tree = ttk.Treeview(window, columns=('Date', 'Amount', 'Category', 'Store'), show='headings')
tree.heading('Date', text='Date')
tree.heading('Amount', text='Amount')
tree.heading('Category', text='Category')
tree.heading('Store', text='Store')
tree.column('Date', width=100)
tree.column('Amount', width=100)
tree.column('Category', width=150)
tree.column('Store', width=150)
tree.pack(fill=tk.BOTH, expand=True)

# Start the application
window.mainloop()
