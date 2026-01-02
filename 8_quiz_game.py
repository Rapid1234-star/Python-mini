#Quiz Game

questions=(" What is the capital of France? ",
           " What is 2 + 2? ",
           " What is the largest planet in our solar system? ",
           " Who wrote 'Romeo and Juliet'? ",
           " What is the boiling point of water in Celsius? ",
           " What is the chemical symbol for gold? ",
           " What is the chemical symbol for silver? ")

options=(("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
         ("A. 3", "B. 4", "C. 5", "D. 6"),
         ("A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"),
         ("A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. Jane Austen"),
         ("A. 90°C", "B. 100°C", "C. 110°C", "D. 120°C"),
         ("A. Au", "B. Ag", "C. Fe", "D.Pb"),
         ("A. Au", "B. Ag", "C. Fe", "D.Pb"))

answers = ("A", "B", "B", "C", "B", "A", "B")

guesses = []
score = 0
question_num=0

for question in questions:
    print("-------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess=input("Enter (A, B, C, or D): ")
    guesses.append(guess)
    if guess.upper()==answers[question_num]:
        score+=1
        print("CORRECT!\n")
    else:
        print("WRONG!\n")
    question_num+=1

print("-------------------------------")
print("RESULTS")
print("-------------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score=int(score/len(questions)*100)

print(f"Your score is: {score}%")
