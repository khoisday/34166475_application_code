import random

# Functiont to generate a random number between 1 and 100
def generate_random_number():
    return random.randint(1, 100)

# Function to get user guess and validate the input
def get_user_guess():
    #Repeat until find a valid input to return
    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a valid number between 1 and 100.")
        # Handle errors with not integer input
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to handle with user feedback     
def user_feedback(target_number):
    
    # Repeat until get the target_number
    while True:
        user_guess = get_user_guess()
        if user_guess < target_number:
            print("Higher! Try again.")
        elif user_guess > target_number:
            print("Lower! Try again.")
        else:
            print("Congratulations! You guessed the correct number:", target_number)
            return

# Main function
def main():
    target_number = generate_random_number()
    user_feedback(target_number)

if __name__ == "__main__":
    main()