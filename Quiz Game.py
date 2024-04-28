'''
A simple quiz game using Tkinter. It displays questions and multiple-choice options on the window,
and the user can select an option by clicking on buttons.
After selecting an option, it checks whether the selected option is correct and moves to the next question.
Once all questions are answered, it displays the final score in a message box.
'''

import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Paris", "Rome", "Berlin"],
                "answer": "Paris"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Leo Tolstoy"],
                "answer": "William Shakespeare"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "answer": "Jupiter"
            }
        ]
        self.current_question = 0
        self.score = 0
        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=('Arial', 14))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=('Arial', 12), width=20, command=lambda idx=i: self.check_answer(idx))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.update_question()

    def update_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        for i in range(4):
            self.option_buttons[i].config(text=question_data["options"][i])

    def check_answer(self, option_index):
        selected_option = self.questions[self.current_question]["options"][option_index]
        correct_answer = self.questions[self.current_question]["answer"]
        if selected_option == correct_answer:
            self.score += 1
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"You scored {self.score} out of {len(self.questions)}!")
        self.root.destroy()

def main():
    root = tk.Tk()
    root.maxsize(500, 400)
    root.minsize(500, 400)
    game = QuizGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
