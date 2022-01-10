import random

def gameMenu():
    print("\nWelcome to \"Guessing a Number Game\"")
    print("Guess my number between 1 and 20")
    print("You have 5 guesses.\n")


def checkUserWannaPlayAgain():
    play_again = input("Play again? Press y to continue or press ENTER to quit: ")
    # loop until user enter 'y' or '' => enter or return
    while not (play_again == "" or play_again == "y"):
        play_again = input("Play again? Press y to continue or press ENTER to quit: ")

    if play_again == "":
        print('Thank you for playing game...\n')
        quit()
    elif play_again == "y":
        return "y"


def checkUserInput(min_vaue, max_value):
    while True:
        guess_num = input("Take a guess : ")
        # handling user input that's whether input is valid int or invalid another
        try:
            guess_num = int(guess_num)
        except ValueError:
            print('* enter integre only\n')
        else:
            if guess_num >= min_vaue and guess_num <= max_value:
                return guess_num
            else:  # this will only excute if guess number is not in range
                print(f'Ps: enter num in a given range {min_vaue} to {max_value}\n')


def startGame():
    # loop throughout the game until the user enter or return
    while True:
        MAX_GUESS = 20
        MIN_GUESS = 1
        # generate random number from 1 to 20
        random_num = random.randint(MIN_GUESS, MAX_GUESS)
        guess_count = 0  # to count user guesses
        flag = None
        while True:
            user_guess = checkUserInput(MIN_GUESS, MAX_GUESS)
            guess_count += 1  # increase one at a time when user enter valid number

            if user_guess == random_num:
                if guess_count == 1:
                    print(f"You got it in {guess_count} guess")
                else:
                    print(f"You got it in {guess_count} guesses")
                flag = True
            elif guess_count == 5:
                print(f"You didn't get it in {guess_count} guesses.")
                print(f"The correct answer is: {random_num}")
                flag = True
            elif user_guess > random_num:
                print("Your guess is too high")
            elif user_guess < random_num:
                print("Your guess is too low")

            # guess is right or didn't get it in 5 guesses
            if flag:
                print()
                if checkUserWannaPlayAgain() == "y":
                    gameMenu()
                    break


gameMenu()
startGame()