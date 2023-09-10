import tkinter as tk

# Function to perform the selected operation
def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                result_label.config(text="Cannot divide by zero")
                return
            result = num1 / num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input. Enter valid numbers.")

# Function to clear input fields and result label
def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields for numbers
entry_num1 = tk.Entry(root)
entry_num1.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

# Create buttons for each operation
operations = ["Add", "Subtract", "Multiply", "Divide"]
for operation in operations:
    button = tk.Button(root, text=operation, command=lambda op=operation: calculate(op))
    button.pack()

# Create a button to clear input fields and result
clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
