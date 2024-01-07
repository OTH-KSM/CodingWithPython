#!/usr/bin/env python3

# ************ While Loop ************************
def while_loop():
    i = 1
    while i <= 10:
        print(i)
        i += 1
    print("DONE")

# Static Guessing Game

def guess_game():
    print("Welcome to the Guessing Game!")
    print("You have to guess the correct word.")
    print("You have 10 tries to guess the word correctly. Good luck!\n")

    word = "animal"
    i = 0
    while i < 10:
        guess = input("Enter the Word : ")
        if guess == word:
            print("Congratulations You Guessed the Word 🥳")
            continu = input("You Want to try again (Y/N) : ")
            if continu == "Y":
                i = -1
            elif continu == "N":
                exit ()
            else:
                print("invalid input")
                exit ()
        else:
            print("Naaaah 😕")
        i += 1

    print("Game Over 🎮 -> 🚫")

# ************* For Loop *************************

def for_loop():
        # For string
    for letter in "Othmane":
        print(letter)

        # For array
    friends = ["Jim", "Lara", "Mike"]
    for friend in friends:
        print(friend)

        # For integers
    for i in range(1, 10):
        print(i)