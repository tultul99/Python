
import random

x = 20
random_number = random.randint(1,x)

guess = 0

while guess != random_number :
    guess = int(input(f"Guess a number between 1 - {x}: "))

    if guess < random_number:
        print("Too low!! Try again\n")
    elif guess > random_number:
        print("Too high!! Try again\n")
        
print(f"Congratulations!!! You guess the correct number {random_number}\n")

    