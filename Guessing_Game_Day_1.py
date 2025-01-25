
#This prompts the user to input his/her name
name = input("What is your name?  " )
print(f"Hello, {name}! Welcome to the Guessing game!")
print("A random number from 1-100 will be chosen by the gnarly goblin and you have 7 attempts to guess correctly.")
import time 
import random
start_time = time.time()
# After the game ends:

# Loop to restart the game
while True:
    # Generate a random number between 1 and 100
    num = 0
    while num < 1 or num > 100:
        num = random.random() * 100 + 1
        num = round(num)
    
    threshold = 20
    max_guesses = 7  # Set the maximum number of guesses
    print("May the odds be in your favor!")
   
    for i in range(1, max_guesses + 1):
        while True:
            try:
                user = int(input("Please, enter your number: "))
                break
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        
        if user < num:
            if abs(user - num) >= threshold:
                print("Too low. Try again!")
            else:
                print("Low. Goblin says you are closer than you think!")
        elif user > (num + threshold):
            print("Too high. Go lower this time.")
        elif user > num:
            print(f"High. Aim a little lower, {name}.")
        else:
            print(f"Correct! You guessed it in {i} attempts. The mathematical forces are indeed with you.")
            break  # Exit the loop if the user guesses correctly
        
        # Notify the user when they've exhausted their guesses
        if i == max_guesses:
            print("Oops! You have exhausted your guesses potion, better luck next time!")
            print(f"The correct number was {num}.")
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
    print(f"You took {elapsed_time} seconds to play!")
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print(f"Thank you for playing, {name}! Goodbye!")
    break  # Exit the outer loop to end the game


