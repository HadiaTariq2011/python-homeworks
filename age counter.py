age_input = input("Enter your age: ")

if age_input.isdigit():
    age = int(age_input)
    
    if 0 < age <= 120:
        print("Your age is valid.")
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")
    else:
        print("Error: Age must be between 1 and 120.")
else:
    print("Error: Please enter a valid number for age.")
