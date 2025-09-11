import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        # Get user inputs
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        # Calculate product
        product = num1 * num2
        
        # Show result
        messagebox.showinfo("Product Result", f"The product is: {product}")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Multiplication App")
root.geometry("300x250")

# Labels
label1 = tk.Label(root, text="Enter first number:", font=("Arial", 10))
label1.pack(pady=5)
entry1 = tk.Entry(root, width=20, font=("Arial", 12))
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter second number:", font=("Arial", 10))
label2.pack(pady=5)
entry2 = tk.Entry(root, width=20, font=("Arial", 12))
entry2.pack(pady=5)

# Button
button = tk.Button(root, text="Calculate Product", command=calculate_product, bg="lightgreen")
button.pack(pady=20)

# Run the app
root.mainloop()
