import tkinter as tk

window = tk.Tk()
window.title("Finance Tracker")
window.geometry("300x200")

label = tk.Label(window, text="Transaction Entry")
label.pack(pady=10)

first_field = tk.Entry(window, font=('Arial', 14))
first_field.pack(pady=20)


entered_text = "Entry Text"


# Handlers
def first_handler():
  print("First Button was Clicked")

def handle_entry():
  print('Submit Clicked')
  entered_text = first_field.get()

button = tk.Button(window, text="Submit", command=handle_entry)
button.pack(pady=10)

entry_label = tk.Label(window, text=entered_text)
entry_label.pack(pady=30)





window.mainloop()