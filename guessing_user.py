#!/usr/bin/env python3
import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            c_guess = random.randint(low, high)
        else:
            c_guess = low
        feedback = input(f"Is {c_guess} too high (h), too low (l), or correct (c)?: ")
        feedback = feedback.lower
        if feedback == "h":
            high = c_guess - 1
        elif feedback == "l":
            low = c_guess + 1
    print(f"The computer guessed your number, {c_guess}, correctly!!")


# This is in case the user inputs something invalid or something else goes wrong
while True:
    try:
        max_guess = int(input("What should the max guess be?: "))
        break
    except TypeError:
        print("That's not a number!!!")
    except:
        print("Something went wrong...")



computer_guess(max_guess)
