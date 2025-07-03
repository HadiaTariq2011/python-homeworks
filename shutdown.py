def shutdown(command):
    # Convert command to lowercase to handle YES/yes/Yes
    command = command.lower()
    
    if command == "yes":
        return "Shutting down..."
    elif command == "no":
        return "Shutdown aborted."
    else:
        return "Sorry, I don't understand your command."

# Example: getting input from user
user_input = input("Do you want to shut down the system? (yes/no): ")
result = shutdown(user_input)
print(result)
