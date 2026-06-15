# PROJECT 1: SNAKE, WATER, GUN GAME
# We all have played snake, water gun game in our childhood. If you haven’t, google the
# rules of this game and write a python program capable of playing this game with the
# user.
import random
computer = random.choice(["Snake", "Water", "Gun"])
player = input("Enter Your Choice: \n1.Snake \n2.Water \n3.Gun\n")
if computer == player:
    print("It's a tie")
elif computer == "Snake" and player == "Water":
    print("Computer Wins")
elif computer == "Water" and player == "Gun":
    print("Computer Wins")
elif computer == "Gun" and player == "Snake":
    print("Computer Wins")
elif computer == "Water" and player == "Snake":
    print("Player Wins")
elif computer == "Gun" and player == "Water":
    print("Player Wins")
elif computer == "Snake" and player == "Gun":
    print("Player Wins")


# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.
# Hint: Use the random module.

import random
n = random.randint(1,100)
guesses = 1
a = -1
while(a != n):
    a = int(input("Enter Your Guess: "))
    if a > n:
        print("Lower Number Please")
    elif a < n:
        print("Higher Number Please")
    else:
        print (f"The number was {n}. You Guessed It In {guesses} Attempts")
    guesses += 1