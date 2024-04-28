'''
This Program allows the user to play Rock, Paper, Scissors against the computer.
The user inputs their choice, and the computer randomly selects its choice.
The winner is then determined based on the rules of the game,
And you can play the game as many times as you want.
'''

import random
import time

print(" ---------------------")
print("| Rock Paper Scissors |")
print(" ---------------------")
list_Ch = ["R", "P", "S"]
user_Score = 0
computer_Score = 0
i = 1
# How many times you play this game?
chance = int(input("How many time you want to play (no. of chances): "))
while i <= chance:
    computer_Ch = str(random.choice(list_Ch))
    # Take input from user
    user_Ch = input("Enter Rock, Paper, Scissors (key to press: R,P,S): ").upper()
    time.sleep(2)
    if user_Ch == computer_Ch:
        print("Tie You Both Entered Same")
    elif user_Ch == "R":
        print("Computer Enter: ", computer_Ch)
        if computer_Ch == "P":
            print("You lose! Paper covers Rock")
            computer_Score += 1
        else:
            print("You win! Rock smashes Scissors")
            user_Score += 1
    elif user_Ch == "P":
        print("Computer Enter: ", computer_Ch)
        if computer_Ch == "S":
            print("You lose! Scissor cut Paper")
            computer_Score += 1
        else:
            print("You win! Paper covers Rock")
            user_Score += 1
    elif user_Ch == "S":
        print("Computer Enter: ", computer_Ch)
        if computer_Ch == "R":
            print("You lose! Rock smashes Scissors")
            computer_Score += 1
        else:
            print("You win! Scissor cut Paper")
            user_Score += 1
    else:
        print(":")
    print("\n\t******ScoreBoard******")
    print(f"\t You: {user_Score} | Computer: {computer_Score}")
    print("\t**********************")
    print(f"Game No:[{i}]")
    print("========================================================")
    i += 1
print("\n##### Game Over #####")
print("*******************************************")
if user_Score < computer_Score:
    print(
        "Sorry You lose the game \n computer win the game with score:", computer_Score)
elif user_Score == computer_Score:
    print("Game is Tie Play Again")
else:
    print("You Win the Game with score:", user_Score)