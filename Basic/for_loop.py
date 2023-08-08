
for letter in "Rakibul Islam Shanto":
    print (letter)

print ("\n***********************\n")

friends = ["Samsun", "Naher", "Asme"]
for name in friends:
    print (name)

print ("\n***********************\n")

for index in range(10) :
    print(index+1)

print ("\n***********************\n")

for index in range(5, 10) :
    print(index)

print ("\n***********************\n")

friends = ["Samsun", "Naher", "Asme"]
for index in range(len(friends)) :
    print(index)
    print(friends[index])

print ("\n***********************\n")

for index in range(5) :
    if index == 0:
        print ("First iteration")
    else :
        print ("Not first iteration")