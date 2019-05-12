###### Name: Shivika Varshney
# Description: A guessing game!
import random 

name = input("Hello! What is your name?")
number = random.randint(1, 100)
print("Hi " + name + "! I'm thinking of a number between 1 and 100. Can you guess what it is? Remember, you only have 5 guesses!")
guessesTaken = 0

while guessesTaken < 6: 
    guess = input("Enter a guess:")
    guess = int(guess)
    guessesTaken = guessesTaken + 1 
    if guess-number == number:
        print("Congratulations " + name + "! You guessed the correct number!")
    elif guess-number <= 5 and guess-number >= -5:
        print("You are so close!")
    elif guessesTaken > 5: 
        print("Aw man " + name + "! The right number was", number)
    elif guess < number:
        print("Sorry! The number is too low!")
    elif guess > number: 
        print("Sorry! The number is too high!")  
    else:
        break 
