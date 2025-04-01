
#THIS PROJECT IS A SIMPLE GAME OF DICE ROLLING SIMULATION
#THE GAME WILL BE PLAYED BETWEEN THE COMPUTER AND THE USER
#THE COMPUTER WILL RANDOMLY SELECT A MOVE AND THE USER WILL BE PROMPTED TO ENTER THEIR MOVE
#THE GAME WILL THEN DETERMINE THE WINNER AND DISPLAY THE RESULT
#THE GAME WILL CONTINUE UNTIL THE USER CHOOSES TO QUIT

import random
input("Welcome to the Dice Rolling Simulation! Press Enter to roll the dice.")
print("The rules are simple:")
print("You will roll two dice.")
print("If the sum of the two dice is 7, you win!")
print("If the sum of the two dice is 2, you lose.")
print("If the sum of the two dice is anything else, it's a tie.")
print("Let's start the game!")
print("Press Enter to roll the dice.")
input()
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print("You rolled a", dice1, "and a", dice2)
sum_of_dice = dice1 + dice2
if sum_of_dice == 7:
    print("Congratulations! You rolled a 7. You win!")
elif sum_of_dice == 2:  
    print("Sorry, you rolled a 2. You lose.")
else:
    print("It's a tie! You rolled a", sum_of_dice)
print("Thanks for playing!")
