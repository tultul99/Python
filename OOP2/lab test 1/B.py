
li = []
n = int(input("Enter a range: "))
i = 0
while n>i :
    li.append(int(input()))
    i += 1

if len(li)<4 :
    print("Not possible")
else:
    rakib = li.copy()
    rakib.pop()
    rakib.pop()
    rakib.reverse()
    rakib.pop()
    rakib.pop()
    print(rakib)
