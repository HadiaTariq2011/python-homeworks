import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        # Get inputs
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())

        # Simple Interest Formula
        si = (principal * time * rate) / 100

        # Compound Interest Formula
        ci = principal * ((1 + rate/100) ** time) - principal

        # Show results
        result_label.config(
            text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}"
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")

# Create main window
window = tk.Tk()
window.title("Simple & Compound Interest Calculator")
window.geometry("400x300")

# Principal input
label_principal = tk.Label(window, text="Principal Amount:", font=("Arial", 12))
label_principal.pack(pady=5)
entry_principal = tk.Entry(window, font=("Arial", 12))
entry_principal.pack(pady=5)

# Time input
label_time = tk.Label(window, text="Time (in years):", font=("Arial", 12))
label_time.pack(pady=5)
entry_time = tk.Entry(window, font=("Arial", 12))
entry_time.pack(pady=5)

# Rate input
label_rate = tk.Label(window, text="Rate of Interest (%):", font=("Arial", 12))
label_rate.pack(pady=5)
entry_rate = tk.Entry(window, font=("Arial", 12))
entry_rate.pack(pady=5)

# Calculate button
button = tk.Button(window, text="Calculate", command=calculate_interest, font=("Arial", 12), bg="lightgreen")
button.pack(pady=10)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Run the app
window.mainloop()
