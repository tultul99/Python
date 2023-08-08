a, b, c = 5, 3.2, "Hello"

print (a, b, c)
print (b)
print (c)

print(type(a))
print(type(b))
print(type(c))

###########

print (000)
print (2.3)
print (-33)
print (3+5)
print (3+5.5)
print (3+5.5*2)
print ((3+5.5)*2)
print (5%2)

num = 10
print(str(num))
print(num , "is a number")
print(str(num) + " is a number")

n = -5
print (abs(n))

print (pow(3, 2))

print (max (3,8))
print (min (3,8))

print (round (3.8))
print (round (3.3))

from math import *
print (floor(3.7))
print (ceil(3.7))
print (ceil(3.2))

print (sqrt(64))

###########

ss = "Rakibul Islam"

print (ss.upper())
print (ss.isupper())
print (ss.lower())
print (ss.lower().islower())

ss = "shanto"
print (ss, "is lower? ->" , ss.islower())

ss = "Rakibul Islam Shanto"
print (len(ss))  

print (ss[0])      
print (ss.index("R")) 

print (ss[4])
print (ss.index("b"))

print (ss.index("Sha"))  

print (ss.replace("Shanto", "SHANTO"))

ss = "shanto"
print (ss.isalpha())

###########

i = 0

while i<10:
    print (i+1)
    i += 1


###########

print ("2^3", 2**3)

def power (base, power) :
    i = int(power)
    result = 1
    while i != 0 :
        result *= base
        i -= 1
    return result 

a, b = input("Enter base : "), input ("Enter power: ")
print ("Result =",power(int(a), int(b)))


###########


for index in range(5, 10) :
    print(index)

print ("\n***********************\n")

friends = ["Rakibul", "Islam", "Shanto"]

for index in range(len(friends)) :
    print(index)
    print(friends[index])

print ("\n***********************\n")

for index in range(5) :
    if index == 0:
        print ("First iteration")
    else :
        print ("Not first iteration")

###########

def shanto (name) :
    print(name)
    print ("Welcome.")

print ("Hi")

shanto()

###########

sum = 0
i = 1
while i<=100 :
    sum += i
    if i == 100 :
        print(i, "=" , sum , end="")
    else :
        print(i , "+ " , end="")
    i += 1

###########

a,b,c = int(input('Enter 3 ages: ')), int(input()), int(input())

old = max(a,b,c)
young = min(a,b,c)

print(f'The oldest age is {old} and the youngest age is {young}')

###########

mark = int(input("Enter your marks: "))

if mark<=100 and mark>=80:
    print(f'Garde: A+, Remark: Outstanding!')

elif mark<=79 and mark>=75:
    print(f'Garde: A, Remark: Excellent!')

elif mark<=74 and mark>=70:
    print(f'Garde: A-, Remark: Very good!')

elif mark<=69 and mark>=65:
    print(f'Garde: B+, Remark: Good!')

elif mark<=64 and mark>=60:
    print(f'Garde: B, Remark: Satisfactory!')

elif mark<=59 and mark>=55:
    print(f'Garde: B-, Remark: Above average!')

elif mark<=54 and mark>=50:
    print(f'Garde: C+, Remark: Average!')

elif mark<=49 and mark>=45:
    print(f'Garde: C, Remark: Bellow average!')

elif mark<=44 and mark>=40:
    print(f'Garde: D, Remark: Pass!')

elif mark<=39 and mark>=00:
    print(f'Garde: F, Remark: Fail!')

###########

