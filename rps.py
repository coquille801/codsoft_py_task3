import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors:")
        self.label.pack(pady=10)

        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play("Rock"))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play("Paper"))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play("Scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(self.root, text="Result: ")
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(self.root, text="User: 0 | Computer: 0")
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        result = self.determine_winner(user_choice, computer_choice)
        self.result_label.config(text=f"User chose: {user_choice} | Computer chose: {computer_choice}\n{result}")

        if "User wins" in result:
            self.user_score += 1
        elif "Computer wins" in result:
            self.computer_score += 1

        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.computer_score}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            return "User wins!"
        else:
            return "Computer wins!"

    def reset_game(self):
        self.result_label.config(text="Result: ")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="User: 0 | Computer: 0")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
