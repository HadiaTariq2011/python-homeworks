# Program to calculate power using a loop

# Get input from the user
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent (power): "))

result = 1  # Start with 1 because anything raised to 0 is 1

# Use a loop to multiply base, exponent times
for i in range(exponent):
    result *= base  # Multiply result by base in each iteration

# Print the result
print(f"{base}^{exponent} = {result}")
