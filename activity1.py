import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date

def calculate_age():
    try:
        # Get user input
        dob_str = entry.get()
        
        # Convert input string to datetime object
        dob = datetime.strptime(dob_str, "%d-%m-%Y").date()
        
        # Today's date
        today = date.today()
        
        # Calculate age
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        # Display result
        messagebox.showinfo("Age Calculator", f"Your current age is: {age} years")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter DOB in DD-MM-YYYY format.")

# Create main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")

# Label
label = tk.Label(root, text="Enter your Date of Birth (DD-MM-YYYY):", font=("Arial", 10))
label.pack(pady=10)

# Entry box
entry = tk.Entry(root, width=20, font=("Arial", 12))
entry.pack(pady=5)

# Button
button = tk.Button(root, text="Calculate Age", command=calculate_age, bg="lightblue")
button.pack(pady=20)

# Run app
root.mainloop()
