#madlibs game

def madlibs():
    print("Welcome to the Madlibs game!")
    
    # Collecting user inputs
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    verb1 = input("Enter a verb: ")
    adjective1 = input("Enter an adjective: ")
    place1 = input("Enter a place: ")
    
    # Creating the madlib story
    story = f"Once upon a time in {place1}, there was a {adjective1} {noun1}. Every day, it would {verb1} with its friend, a {noun2}. They had many adventures together!"
    
    # Displaying the story
    print("\nHere is your madlib story:")
    print(story)

madlibs()