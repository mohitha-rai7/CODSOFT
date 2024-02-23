import tkinter as tk

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit", command=self.add_task)
        self.submit_button.pack()

        self.tasks_label = tk.Label(master, text="Tasks:")
        self.tasks_label.pack()

        self.tasks_text = tk.Text(master, height=10, width=50)
        self.tasks_text.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_display()
            self.task_entry.delete(0, tk.END)

    def update_task_display(self):
        self.tasks_text.delete(1.0, tk.END)
        for task in self.tasks:
            self.tasks_text.insert(tk.END, f"- {task}\n")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


