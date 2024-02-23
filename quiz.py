import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz")
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Jupiter", "Mars", "Saturn"],
                "answer": "Mars"
            },
            {
                "question": "What is the largest mammal?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "answer": "Blue Whale"
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(master, text="")
        self.question_label.pack()
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(master, text="", command=lambda i=i: self.check_answer(i))
            button.pack(fill=tk.BOTH, expand=True)
            self.option_buttons.append(button)
        
        self.next_question()
    
    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i])
            self.current_question += 1
        else:
            messagebox.showinfo("Quiz Completed", f"Your score is {self.score}/{len(self.questions)}")
            self.master.destroy()
    
    def check_answer(self, selected_option):
        question_data = self.questions[self.current_question - 1]
        selected_answer = question_data["options"][selected_option]
        correct_answer = question_data["answer"]
        if selected_answer == correct_answer:
            self.score += 1
        self.next_question()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
