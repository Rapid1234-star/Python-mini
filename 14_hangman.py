# Hangman Game
import random

words = (
    "python", "java", "kotlin", "javascript", "hangman",
    "programming", "developer", "function", "variable", "condition"
)

hangman_art = {
    0: (
        "  +---+",
        "      |",
        "      |",
        "      |",
        "      |",
        "      |",
        "========="
    ),
    1: (
        "  +---+",
        "  O   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "========="
    ),
    2: (
        "  +---+",
        "  O   |",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "========="
    ),
    3: (
        "  +---+",
        "  O   |",
        " /|   |",
        "      |",
        "      |",
        "      |",
        "========="
    ),
    4: (
        "  +---+",
        "  O   |",
        " /|\\  |",
        "      |",
        "      |",
        "      |",
        "========="
    ),
    5: (
        "  +---+",
        "  O   |",
        " /|\\  |",
        " /    |",
        "      |",
        "      |",
        "========="
    ),
    6: (
        "  +---+",
        "  O   |",
        " /|\\  |",
        " / \\  |",
        "      |",
        "      |",
        "========="
    )
}

def display_hangman(wrong):
    print("\n")
    for line in hangman_art[wrong]:
        print(line)
    print()

def display_hint(hint):
    print("Word:", " ".join(hint))
    print()

def display_answer(answer):
    print("Answer:", " ".join(answer))
    print()

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("\n⚠️ Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("\n⚠️ You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"\n❌ Wrong guess! Attempts left: {6 - wrong_guesses}\n")

        if "_" not in hint:
            print("\n🎉 Congratulations! You guessed the word!\n")
            display_answer(answer)
            is_running = False

        elif wrong_guesses == 6:
            display_hangman(wrong_guesses)
            print("\n💀 Game Over! You've been hanged.\n")
            print(f"The correct word was: {answer}\n")
            is_running = False

if __name__ == "__main__":
    main()
