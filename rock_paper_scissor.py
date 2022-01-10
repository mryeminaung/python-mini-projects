"""
Rock smashes scissors.
Paper covers rock.
Scissors cut paper.

Creater : Ye Min Aung
Date : 17 / 7 / 2021
Project Name: rock paper scissor
"""

import random

possible_actions = ["rock", "paper", "scissors"]

while True:
    print("\n\t====>>>>>>> ROCK, PAPER, SCISSOR <<<<<<<====\n")

    user_choice = input("Enter a choice (rock, paper, scissors) : ")
    computer_action = random.choice(possible_actions)

    while user_choice not in possible_actions:
        print("Invalid choice!!\n")
        user_choice = input("Enter a choice (rock, paper, scissors) : ")

    print("Computer : {}\nUser : {}\n".format(computer_action, user_choice))

    if user_choice == computer_action:
        print(f"You and Computer selected : {user_choice}. It's draw.")
    elif user_choice == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors.! You win.")
        elif computer_action == "paper":
            print("Paper covers rock.! You lose.")
    elif user_choice == "paper":
        if computer_action == "rock":
            print("Paper covers rock.! You win.")
        elif computer_action == "scissors":
            print("Scissors cut paper.! You lose.")
    elif user_choice == "scissors":
        if computer_action == "paper":
            print("Scissors cut paper.! You win.")
        elif computer_action == "rock":
            print("Rock smashes scissors.! You lose.")

    play_again = input("\nDo you want to play again? (y/n) => ").lower()

    while not (play_again == 'y' or play_again == 'n'):
        print("* just enter 'y' or 'n'")
        play_again = input("\nDo you want to play again? (y/n) => ")

    if play_again == 'y':
        continue
    else:
        print("Good Game...")
        break