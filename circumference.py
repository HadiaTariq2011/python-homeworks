import math

# Define a function to calculate circumference
def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

# Get radius from the user
r = float(input("Enter the radius of the circle: "))

# Call the function and display the result
result = calculate_circumference(r)
print(f"The circumference of the circle is: {result:.2f}")
