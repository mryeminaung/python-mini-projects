"""
Name = Ye Min Aung
Date = 11 / 30 / 2020
Project name = dice rolling game
"""
import random
import time

draw = 0
round = 1
player1 = 0
player1_win = 0
player2 = 0
player2_win = 0
print("\n\t\tWelcome From the Dice Rolling Game")
print("\t\t----------------------------------\n")
while round != 11:  # loop until round == 11

    print("\tRound", round)
    player1 = random.randint(1, 6)
    time.sleep(1)
    player2 = random.randint(1, 6)
    time.sleep(1)

    print(f"Player1's score: {player1}")
    print(f"Player2's score: {player2}")

    if player1 == player2:
        print("\t* Draw")
        print("--------------------------\n")
        draw += 1
    elif player2 > player1:
        print("\t* Player2 wins.")
        print("--------------------------\n")
        player2_win += 1
    else:
        print("\t* Player1 wins.")
        print("--------------------------\n")
        player1_win += 1

    round += 1  # update the loop counter

print(f"Player1 wins {player1_win} times.")
print(f"Player2 wins {player2_win} times.")
print(f"Player1 and Player2 draw {draw} times.\n")

if player1_win == player2_win:
    final_result = "Draw"
elif player2_win > player1_win:
    final_result = "Player2 wins this game"
else:
    final_result = "Player1 wins this game"

print(f"Final result : {final_result}.")
print("\n------------Enjoy with Coding--------------\n")