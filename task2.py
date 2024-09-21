import random

def guess_the_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0
    guess = None
    
    print("Welcome to the Guess the Number Game!")
    print("I have selected a random number between 1 and 100.")
    
    # Continue prompting the user until they guess correctly
    while guess != random_number:
        # Get the user's guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Provide feedback based on the user's guess
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {random_number} correctly!")
                print(f"It took you {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
guess_the_number()
