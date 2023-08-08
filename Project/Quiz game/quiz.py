
ans = input("Do you want to give the test? ").upper()        # yes  Yes  yEs   ==  YES

if ans != 'YES' :
    quit()

print("\n\tWelcome to quiz game\n")
name = input('Enter your name: ')
print(f"Let's start {name}!!")

score = 0
ans = input("\n1. What does RAM stand for? ").lower()       #  Random  random  RANDOM
if ans == 'random access memory':
    print('Correct!')
    score += 1
else :
    print('Wrong!')

ans = input("2. What does ROM stand for? ").lower()
if ans == 'read only memory':
    print('Correct!')
    score += 1
else :
    print('Wrong!')

ans = input("3. What does CPU stand for? ").lower()
if ans == 'central processing unit':
    print('Correct!')
    score += 1
else :
    print('Wrong!')

ans = input("4. What does HTTP stand for? ").lower()
if ans == 'hyper text transfer protocol':
    print('Correct!')
    score += 1
else :
    print('Wrong!')

ans = input("5. What does GPU stand for? ").lower()
if ans == 'graphics processing unit':
    print('Correct!')
    score += 1
else :
    print('Wrong!')

print(f"\nYour total score is {score}")
print(f"You give {(score / 5) * 100} % correct answer.")
print(f"\n\tThank you for playing {name}.\n")
