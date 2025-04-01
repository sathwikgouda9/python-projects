
#THIS PROJECT IS A SIMPLE GAME OF ROCK PAPER SCISSORS
#THE GAME WILL BE PLAYED BETWEEN THE COMPUTER AND THE USER
#THE COMPUTER WILL RANDOMLY SELECT A MOVE AND THE USER WILL BE PROMPTED TO ENTER THEIR MOVE
#THE GAME WILL THEN DETERMINE THE WINNER AND DISPLAY THE RESULT
#THE GAME WILL CONTINUE UNTIL THE USER CHOOSES TO QUIT
#THE GAME WILL KEEP TRACK OF THE SCORE AND DISPLAY IT AT THE END
#THE GAME WILL ALSO DISPLAY THE RULES OF THE GAME AND HOW TO PLAY

Choice = ["rock", "paper", "scissors"]
import random
Choice = random.choice(Choice)
print("Welcome to the game of Rock Paper Scissors")
print("The rules are simple:")
print("Rock beats scissors")
print("Scissors beats paper")
print("Paper beats rock")
print("You will be prompted to enter your move")
print("If you want to quit the game, type 'quit'")
print("Let's start the game!")
print("Enter your move:")
user = input()
if user == "rock":
    if Choice == "rock":
        print("It's a tie!")
    elif Choice == "paper":
        print("Paper beats rock! You lose!")
    else:
        print("Rock beats scissors! You win!")
elif user == "paper":
    if Choice == "rock":
        print("Paper beats rock! You win!")
    elif Choice == "paper":
        print("It's a tie!")
    else:
        print("Scissors beats paper! You lose!")
elif user == "scissors":
    if Choice == "rock":
        print("Rock beats scissors! You lose!")
    elif Choice == "paper":
        print("Scissors beats paper! You win!")
    else:
        print("It's a tie!")
elif user == "quit":
    print("Thanks for playing!")
else:
    print("Invalid move! Please try again.")        