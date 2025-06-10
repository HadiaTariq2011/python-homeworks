# Program to convert decimal to binary using nested loops

# Get input from the user
decimal = int(input("Enter a decimal number: "))

binary = ""  # String to store binary digits

# Outer loop (only runs once in this simple case, but used here to show nested loop usage)
for i in range(1):
    num = decimal
    # Inner loop to perform the conversion
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary  # Build the binary string
        num = num // 2

# If the number was 0, binary should also be 0
if binary == "":
    binary = "0"

# Print the result
print("Binary number:", binary)
