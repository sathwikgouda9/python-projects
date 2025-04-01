# This project is based on number gussing game in this you get 3 choice to guess the number
# and if you guess the number in 3 chances you win otherwise you lose. So let's start coding.
import random
guessnumber = random.randint(1, 10)  
print("Welcome to the game of Guess the number")
print("I have selected a number between 1 and 10. Can you guess it?")
print("You have 3 chances to guess the number.")
print("If you guess the number in 3 chances you win otherwise you lose.")
print("Let's start the game!")
userguess= int(input("Enter your guess: "))
if userguess == guessnumber:
    print("Congratulations! You guessed the number correctly.")
else:
    print("Sorry, that's not the correct number.")
    userguess= int(input("Enter your guess: "))
    if userguess == guessnumber:
        print("Congratulations! You guessed the number correctly.")
    else:
        print("Sorry, that's not the correct number.")
        userguess= int(input("Enter your guess: "))
        if userguess == guessnumber:
            print("Congratulations! You guessed the number correctly.")
        else:
            print("Sorry, that's not the correct number.")
            print(f"The correct number was {guessnumber}. Better luck next time!")
            print("Thanks for playing!")
            print("Goodbye!")
            print("Have a great day!")

            
