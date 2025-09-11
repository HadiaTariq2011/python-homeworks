import tkinter as tk
import random

def change_colors(event):
    """Custom event handler to change stripe colors"""
    # Random colors
    colors = ["red", "green", "blue", "yellow", "orange", "purple", "cyan", "pink"]
    
    canvas.itemconfig(stripe1, fill=random.choice(colors))
    canvas.itemconfig(stripe2, fill=random.choice(colors))

# Create main window
root = tk.Tk()
root.title("Stripe Color Changer")
root.geometry("400x300")

# Create canvas
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Draw two stripes
stripe1 = canvas.create_rectangle(50, 50, 350, 100, fill="blue")
stripe2 = canvas.create_rectangle(50, 150, 350, 200, fill="red")

# Bind custom event (when pressing 'c', colors will change)
root.bind("<c>", change_colors)

# Instruction label
label = tk.Label(root, text="Press 'c' to change stripe colors", font=("Arial", 12))
label.pack(pady=10)

# Run app
root.mainloop()
