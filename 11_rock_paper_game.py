#Rock Paper Game
import random
options = ["rock", "paper", "scissors"]

player=None
computer=random.choice(options)
running=True
score_player=0
score_computer=0

while running:
    while player not in options:
        player=input("Enter your choice (rock, paper, scissors): ").lower()

    print()
    print(f"Player chose: {player}")
    print(f"Computer chose: {computer}")
    print()


    if player==computer:
        print("It's a tie!")

    elif (player=="rock" and computer=="scissors") or \
        (player=="paper" and computer=="rock") or \
        (player=="scissors" and computer=="paper"):
        print("Player wins!")
        score_player+=1

    else:
        print("Computer wins!")
        score_computer+=1
        
    print()
    play_again=input("Play again? (Y/N): ").lower()

    if play_again!="y":
        running=False

    player=None
    computer=random.choice(options)

print("Game Over.")
print(f"Final Scores ")
print(f"Player: {score_player} | Computer: {score_computer}")



