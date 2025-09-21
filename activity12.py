import tkinter as tk
import random

# Game logic
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(
        text=f"Your Choice: {user_choice}\nComputer's Choice: {computer_choice}\nResult: {result}"
    )

# Create main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x300")

# Title label
title = tk.Label(window, text="Rock-Paper-Scissors", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Buttons for user choices
frame = tk.Frame(window)
frame.pack(pady=20)

btn_rock = tk.Button(frame, text="Rock", width=10, command=lambda: play("Rock"))
btn_rock.grid(row=0, column=0, padx=10)

btn_paper = tk.Button(frame, text="Paper", width=10, command=lambda: play("Paper"))
btn_paper.grid(row=0, column=1, padx=10)

btn_scissors = tk.Button(frame, text="Scissors", width=10, command=lambda: play("Scissors"))
btn_scissors.grid(row=0, column=2, padx=10)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

# Run app
window.mainloop()
