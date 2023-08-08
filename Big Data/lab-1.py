# value = input('Enter the course code: ')
# value = int(value)

value = 413
print(f"Big Data, CSE-{value}")


print("\n\n-------condition-------")


if value == 413:
    print(f"Theory")
elif value == 414:
    print(f"Lab")
else:
    print(f"outline")



print("\n\n-------list-------")


l = ['big', 'data', 3882, 3871]
print(l)
print("\n\n--------------")
print(*l)
print("\n\n-------for loop-------")

for index in l:
    print(index)

print("\n\n-------for loop 2x value-------")

for index, value in enumerate(l):   # value + index of that value
    print(index, value)


print("\n\n-------range 1-------")


for a in range(5):
    print(a)

print("\n\n-------range 2-------")

for a in range(2, 5):
    print(a)


print("\n\n-------range 3-------")

for a in range(2, 21, 2):
    print(a)


print("\n\n--------range -3 ------")

for a in range(20, -5, -2):
    print(a)


print("\n\n-------set-------")


set = {'big', 'data', 3882, 3871}
print(set)

print("\n\n-------tuples-------")


tup = ('big', 'data', 3882, 3871)
print(tup)

print("\n\n-------dictionary-------")


dic = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
}

print(dic)

print("")

for key, value in dic.items():
    print(key, value)
