
import random

reply = ''
high = int(input("Range = "))
low = 1

while reply != 'c' :
    
    guess = random.randint(low,high)

    reply = input(f"Is {guess} high(h), low(l) or matched(c)? ")
    
    if reply == 'h':
        high = guess - 1
    elif reply == 'l':
        low = guess + 1

print(f"\nYeeeee..... Computer guessed the correct number {guess}\n")

