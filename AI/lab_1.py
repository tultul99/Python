#...............1.............
a = 3
b = "2"
c = "Shanto"
print(a)
print(f"{b}")
print('{}'.format(c))
#...............2.............
a = 'All'
b = 'is'
c = 'well'
print(f"{a} {b} {c}")
print("{}".format(a),"{}".format(b),"{}".format(c))
#...............3.............
a = 1j
b = 1.5
c = "2"
print(type(a),type(b),type(c))
#...............4.............
a = -2
b = 332165499876544
print(type(a))
print(f"{type(b)}")
#...............5.............
a = 1
b = 3
print(f"{a+b}\n{b-a}\n{a-b+a}")
#...............6.............
print(f"Area of rectangle = {2*3}")
print(f"Area of square = {2*2}")
print(f"Area of cube = {2*2*2}")
#...............7.............
n = int(input('Enter a number: '))
i = 2
j = 0
while i<n:
    if n%i==0:
        j += 1
    i += 1
if j==0:
    print(f'{n} is a prime number.')
else:
    print(f'{n} is not a prime number.')

from cmath import sqrt
from primePy import primes
if primes.check(n) == True:
    print(f"prime number.")
else:
    print(f"prime number.")
#...............8.............
x = 20
y = 10
x, y = y, x
print("x =", x)
print("y =", y)

x=10
y=20
x = x + y
y = x - y
x = x - y
print("x =", x)
print("y =", y)
#...............9.............
n = int(input("Enter a number: "))
if n >= 0:
   if n == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")
#...............10.............
def check(n):
    if n%2==0:
        print('Even number')
    else:
        print('Odd number')
n = int(input('Enter a number: '))
check(n)

def find_Evenodd(num):
    number=(num/2)*2
    if(number==num):
        print(num, "is a even number")
    else:
        print(num, "is a odd number")
num=int(input("Enter a number: "))
find_Evenodd(num)

#......................................
#problem 01
print("Md. Rakibul Islam Shanto")

#problem 02
h, b = float(input("Enter height & base: ")), int(input())
print(f"Area = {.5*h*b}")

#problem 03
a,b,c = 5,3,1
eq1 = (-b+(sqrt((b*2)-4*a*c)))/(2*a)
eq2 = (-b-(sqrt((b*2)-4*a*c)))/(2*a)
print(f"equations: {eq1} & {eq2}")

#problem 04
x,y = int(input('Enter two number: ')), int(input())
x, y = y, x
print("x =", x)
print("y =", y)

#problem 05
import random 
x = random.randint(0,100)
print(f"{x}")

#problem 06
a = 2
b = 3
print(f"add = {a+b}\nsubtract = {b-a}\nProduct = {a*b}")

#problem 07
a,b = int(input("Enter two numbers: ")), int(input())
print(f"Maximum = {max(a,b)}")
