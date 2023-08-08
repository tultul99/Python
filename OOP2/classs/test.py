
from math import *

a = 3882
print(sqrt(a))

print(sin(90))

# s = input("Enter a string: ")
# print(reversed(s))

n = -3
print(abs(-3))

name = "asme"
reversed(name)
print(name)
print(reversed(name))

print(float(2))

print(hex(8))

print(len("Samsun Naher Asme"))

print(max(3,8,2))
print(min(3,8,2))

print(pow(2,4))

print (floor(3.7))

print (ceil(3.7))

print(round(38.82))
print(str(364))
print(type([2,3,4]))


arr = ['a','b','c','d']
print(arr)

arr.append('e')
print(arr)

li = arr.copy()
print(li)

arr.clear()
print(arr)

print(li.count('b'))

li.extend('f')
print(li)

print(li.index('c'))

li.pop()
print(li)

li.remove('d')
print(li)

li.reverse()
print(li)

li.sort()
print(li)


import numpy as np

number = np.array([1,2,3,4,5]) 
print(number)
print(type(number))
array_2d = np.array([[1,2],[2,3]])
print(number.ndim)
print(number.size)
print(np.exp(4))
print(np.power(3,2))
print(np.log10(100))
print(np.multiply(2,3))

a = "Asme"
print(a.lower())
print(a.upper())
print(a.isupper())
print(a.islower())
print(a.isalpha())
print(a.split())
