#Number Guessing Game

import random

lowest_num=1
highest_num=10
guesses=0

answer=random.randint(lowest_num, highest_num)
guess=0
is_running=True

print("Python Number Guessing Game!")

print(f"Guess a number between {lowest_num} and {highest_num}.")

while is_running:
    guess=int(input("Enter your guess: "))
    guesses+=1

    if guess<answer:
        print("Too low! Try again.")

    elif guess>answer:
        print("Too high! Try again.")

    else:
        print("Congratulations! You've guessed the correct number.")
        print(f"The number of guesses {guesses}.")
        is_running=False
    
print("Game Over.")
