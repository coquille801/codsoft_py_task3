import tkinter as tk
from tkinter import messagebox
import string
import random

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.create_widgets()

    def create_widgets(self):
        self.length_label = tk.Label(self.root, text="Enter desired password length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)
        self.length_entry = tk.Entry(self.root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.include_upper = tk.BooleanVar(value=True)
        self.include_lower = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)

        self.uppercase_check = tk.Checkbutton(self.root, text="Include Uppercase Letters", variable=self.include_upper)
        self.uppercase_check.grid(row=1, column=0, columnspan=2)

        self.lowercase_check = tk.Checkbutton(self.root, text="Include Lowercase Letters", variable=self.include_lower)
        self.lowercase_check.grid(row=2, column=0, columnspan=2)

        self.digits_check = tk.Checkbutton(self.root, text="Include Digits", variable=self.include_digits)
        self.digits_check.grid(row=3, column=0, columnspan=2)

        self.special_check = tk.Checkbutton(self.root, text="Include Special Characters", variable=self.include_special)
        self.special_check.grid(row=4, column=0, columnspan=2)

        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, pady=20)

        self.result_label = tk.Label(self.root, text="Generated Password: ")
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showerror("Error", "Password length must be greater than 0")
                return

            character_pool = ""
            if self.include_upper.get():
                character_pool += string.ascii_uppercase
            if self.include_lower.get():
                character_pool += string.ascii_lowercase
            if self.include_digits.get():
                character_pool += string.digits
            if self.include_special.get():
                character_pool += string.punctuation

            if not character_pool:
                messagebox.showerror("Error", "At least one character set must be selected")
                return

            password = ''.join(random.choice(character_pool) for _ in range(length))
            self.result_label.config(text=f"Generated Password: {password}")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for length")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
