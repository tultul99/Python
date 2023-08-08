a = 10      # declared 2 variable
b = 5
if a>b:     # a conddition to check a is greater than b then print the string
    print('Daffodil International University')

#............................................

i = 1      # initialize i = 1
while i<=6:   # it's a loop where the condition is i<=6
    print(i)  # print the value of i
    i += 1    # the increment of i

#............................................
fruits = ['mango', 'apple', 'guava', 'jackfruit']    # declare a list and assign some string
for i in fruits:     # using a for loop to print out every index from the list
    print(i)

#............................................

n = 7
if n>-1:      # condition, n is greater then -1 bcz i have to check if it is positive. 
    print(n,"is a postive number.")

#............................................

list1 = [1,2,3,4,5]   # declare a list of integer numbers
sum = 0               # assign value zero
for x in list1:       # using the for loop to take every index from the list
    sum += x          # sum = sum + x
print("Summation =",sum)

#............................................

i = 1
while i<20:        # the loop will continue untill i is equal or greater than 20
    print(i)
    if i==10:       # when the value of i will be 10 then the loop will break down
        break
    i += 1

#---------------------------------------

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


