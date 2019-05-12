import random

print("Hi! Welcome to Hangman!")
words = ["birthday", "backpack","yak"]
index = random.randint(0, 2) #importing a random word 
letter = (words[index])
numberOfguesses = 1










while numberOfguesses < 7:
    guess = input("Please type in your first letter guess:")
    #intGuess = ord(guess)
    ind=letter.index(guess)
    print(ind)
    if(ind>-1):
        print("___t___")
    numberOfguesses = numberOfguesses + 1
    if guess-index == index:
        print("Congratulations! You guessed the word!")
    elif numberOfguesses > 7:
        print("Aw man! You weren't able to figure out the word! The correct word was:" + index + ".")