def greet(name):
    """
    Generates a personalized greeting message.
    
    Parameters:
    name (str): The name of the user.
    
    Returns:
    str: A personalized greeting message.
    """
    return f"Hello, {name}! Welcome!"

def main():
    """
    Handles user input and prints a personalized greeting.
    """
    # Prompt the user for their name
    user_name = input("Please enter your name: ")
    
    # Generate and print the greeting message
    greeting_message = greet(user_name)
    print(greeting_message)

# Entry point of the script
if __name__ == "__main__":
    main()
