#!/usr/bin/env python3
import random

# This is the part of the code that gets a random integer and then asks the user to guess it
def guess(x):
    # The random integer is generated based on the max number the user previously had to input
    random_number = random.randint(1, x)
    user_guess = 0
    # Here the code checks if the number is the same as the random number
    while user_guess != random_number:
        try:
            user_guess = int(input(f"What do you think is the number between 1 and {max_guess}?: "))
        except TypeError:
            print("Thats not a number...")
        except:
            print("SOMETHING WENT WONGGGG!!!!!")

        if user_guess > random_number:
            print("The number is too big!")
        elif user_guess < random_number:
            print("The number is too small!")
        elif user_guess == random_number:
            print("You got it!")

# This is in case the user inputs something invalid or something else goes wrong
while True:
    try:
        max_guess = int(input("What should the max guess be?: "))
        break
    except TypeError:
        print("That's not a number!!!")
    except:
        print("Something went wrong...")


guess(max_guess)
