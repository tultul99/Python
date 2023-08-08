li = []

i = 0
while 5>i :
    li.append(int(input()))
    i += 1

ra = li.copy()

max = li[0]
for i in li :     
    if i>max :
        max = i

li.remove(max)

max = li[0]
for i in li :     
    if i>max :
        max = i

print(f"My list: {ra}")
print(f"The secod largest number is the list\
is {max} which was found at index {ra.index(max)}.")
