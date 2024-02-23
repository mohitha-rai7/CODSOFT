import tkinter as tk

def add_to_display(character):
    display.insert(tk.END, character)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        clear_display()
        display.insert(tk.END, str(result))
    except Exception as e:
        clear_display()
        display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Simple Calculator")

display = tk.Entry(root, width=20, font=('Arial', 14))
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, command=lambda text=text: add_to_display(text))
    button.grid(row=row, column=col)

clear_button = tk.Button(root, text="C", width=5, height=2, command=clear_display)
clear_button.grid(row=5, column=0, columnspan=2)

calculate_button = tk.Button(root, text="Calculate", width=10, height=2, command=calculate)
calculate_button.grid(row=5, column=2, columnspan=2)

root.mainloop()
