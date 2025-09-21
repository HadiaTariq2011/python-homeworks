import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        messagebox.showwarning("Warning", "Please enter a password!")
        return

    # Strength rules based on length
    if length < 4:
        strength = "Very Weak"
        color = "red"
    elif 4 <= length < 8:
        strength = "Weak"
        color = "orange"
    elif 8 <= length < 12:
        strength = "Strong"
        color = "blue"
    else:
        strength = "Very Strong"
        color = "green"

    result_label.config(text=f"Password Strength: {strength}", fg=color)


# Main window
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("400x200")

# Label
label = tk.Label(window, text="Enter your password:", font=("Arial", 12))
label.pack(pady=10)

# Entry field
entry = tk.Entry(window, font=("Arial", 12), show="*")  # hide input with *
entry.pack(pady=5)

# Button
button = tk.Button(window, text="Check Strength", command=check_strength, font=("Arial", 12), bg="lightblue")
button.pack(pady=10)

# Result
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run app
window.mainloop()
