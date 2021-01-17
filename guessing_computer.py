#!/usr/bin/env python3
import random

def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0
    while user_guess != random_number:
        try:
            user_guess = int(input(f"What do you think is the number between 1 and {max_guess}?: "))
        except:
            print("Thats not a number...")

        if user_guess > random_number:
            print("The number is too big!")
        elif user_guess < random_number:
            print("The number is too small!")
        elif user_guess == random_number:
            print("You got it!")

while True:
    try:
        max_guess = int(input("What should the max guess be?: "))
        break
    except:
        print("That's not a number!!!")

guess(max_guess)
