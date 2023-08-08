
import random

def game():

    computer = random.choice(['r','p','s'])
    user = input("What's your choice?\n \
    Rock(r), paper(p) or scissor(s): ")

    if computer == user :
        print ("It's a tie !!!!")

    elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') \
        or (user == 's' and computer == 'p') :
        print("Congratulations!! You won.")
    else:
        print("Oh!! you lose.")

count = int(input("\nHow many times you wanna play this? "))

for c in range(count):
    game()
