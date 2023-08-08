from posixpath import split


# num1, num2 = input("Enter 1st number: "), input("Enter 2nd number: ") 
num1, num2 = input().split()

num1 = int(num1)
num2 = int(num2)

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print ("Summation:", sum)
print ("Substruction:", sub)
print ("Multiplication:", mul)
print ("Division:", div) 


print ("----------------------------ADVANCE----------------------------")

