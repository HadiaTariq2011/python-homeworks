start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

squares = []
even_squares = []
odd_squares = []

for num in range(start, end + 1):
    square = num ** 2
    squares.append(square)
    
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("All squared values:", squares)
print("Even squared values:", even_squares)
print("Odd squared values:", odd_squares)
