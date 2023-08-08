'''string = 'abcdefghijk'        
print(string)
print(string[5])
lst = list(string)    # string convert into list
lst[5] = 'z'
# print(lst)
string = ''.join(lst) # list convert into string
print(string)
print(string[5])
'''

'''
sum = 0
n = int(input("test case: "))
for i in range(n) :
    x,y = input("Enter 2 integer: ").split()
    x = int(x) ; y = int(y)
    for j in range (x,(x+(y*2))):
        if j%2 != 0:
            sum += j       # 5 + 7 + 9
    print(sum)
    '''
'''
lst = []

for i in range(3):
    lst.append(input("Enter input: "))

print(lst)
v = 0
c = 0
for index in lst :
    for letter in index :
        c += 1
        if letter in "aeiouAEIOU":
            v += 1

print(f"number of character = {c}\n\
Number of vowels = {v}")

# l = ['asme', 'samsun', '0123']

# for index in l:
#     print(index)
#     for letter in index:
#         print(letter)
#     print("\n")
'''

'''
lst = []
for i in range(40,61):
    if i%2 == 0:
        i += 5
    elif i%5 == 0:
        i += 2
    lst.append(i)

print(lst)
'''
'''
def tomar_ja_mon_chay ():
    day = input("Enter a day: ")
    # for day in lst:
    if day.lower() == 'friday':
        print('Today is holiday')
    else :
        print('Working day')

lst = ['saturday', 'sunday', 'tuesday', 'thursday', 'friday']
lst.insert(2,'monday')
lst.insert(4,'wednesday')
# print(lst)
tomar_ja_mon_chay()
'''

'''
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = .5 * base  * height
print(area)
'''

