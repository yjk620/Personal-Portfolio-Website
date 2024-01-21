import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox


class GuessRandomNumberGame:
    def __init__(self):
        # set variables and custumize GUI interface
        self.window = tk.Tk()
        self.window.title("Guess Random Number Game")
        self.window.geometry("400x200")
        self.level = 1
        self.num1 = random.randint(1, 99)
        self.num2 = random.randint(1, 999)
        self.guess = 0
        self.chance = 0

        self.level_label = tk.Label(
            self.window, text=f"Level {self.level}", font=("Press Start 2P", 16))
        self.level_label.pack()

        self.description = tk.Label(
            self.window, text="Guess Any Integer from 1 to 99", font=("Press Start 2P", 12))
        self.description.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.submit_button = tk.Button(
            self.window, text="GUESS", command=self.check_guess)
        self.submit_button.pack()

    def check_guess(self):
        self.guess = self.entry.get()
        if not self.guess.isdigit() or int(self.guess) < 1:
            messagebox.showerror(
                title="Invalid Input", message="Please enter a valid integer.")
            self.entry.delete(0, tk.END)
            return

        self.chance += 1

        if self.level == 1:
            if self.num1 == int(self.guess):
                messagebox.showinfo(
                    title="CORRECT!", message="MOVING ONTO LEVEL 2!")
                self.level += 1
                self.level_label.config(text=f"Level {self.level}")
                self.description.config(
                    text="Guess any integer from 1 to 999:")
                self.chance = 0
            else:
                if int(self.guess) > self.num1:
                    messagebox.showinfo(
                        title="Incorrect Guess", message="Guess a Smaller Number")
                elif int(self.guess) < self.num1:
                    messagebox.showinfo(
                        title="Incorrect Guess", message="Guess a Bigger Number")
                if self.chance == 7:
                    messagebox.showinfo(title="GAME OVER", message="You Lost")
                    self.window.quit()

        if self.level == 2:
            if self.num2 == int(self.guess):
                messagebox.showinfo(title="CONGRATULATIONS", message="WINNER!")
                self.window.quit()
            else:
                if int(self.guess) > self.num2:
                    messagebox.showinfo(
                        title="Incorrect Guess", message="Guess a Smaller Number")
                elif int(self.guess) < self.num2:
                    messagebox.showinfo(
                        title="Incorrect Guess", message="Guess a Bigger Number")
                if self.chance == 10:
                    messagebox.showinfo(title="GAME OVER", message="You Lost")
                    self.window.quit()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = GuessRandomNumberGame()
    game.run()
