import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    name = entry_name.get()
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be a positive integer")
            return
    except ValueError:
        messagebox.showerror("Error", "Password length must be a positive integer")
        return

    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    label_generated_password.config(text="Generated Password: " + password)

def reset_fields():
    entry_name.delete(0, tk.END)
    entry_length.delete(0, tk.END)
    label_generated_password.config(text="Generated Password: ")

root = tk.Tk()
root.title("Password Generator")

frame_input = tk.Frame(root)
frame_input.pack()

label_name = tk.Label(frame_input, text="Enter Name:")
label_name.grid(row=0, column=0, padx=5, pady=5)

entry_name = tk.Entry(frame_input)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_length = tk.Label(frame_input, text="Password Length:")
label_length.grid(row=1, column=0, padx=5, pady=5)

entry_length = tk.Entry(frame_input)
entry_length.grid(row=1, column=1, padx=5, pady=5)

button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=5)

label_generated_password = tk.Label(root, text="Generated Password: ")
label_generated_password.pack(pady=5)

button_reset = tk.Button(root, text="Reset", command=reset_fields)
button_reset.pack(pady=5)

root.mainloop()
