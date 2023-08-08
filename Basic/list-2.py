from posixpath import split


list1 = []

i = 1
while i<=5:
    list1.append(int(input("Enter a value: ")))
    i += 1

print(list1)

n = 'r,a,k,i,b,u,l'
l1 = n.split(",")

# for index in l1:
#     print(index)

s = '1 2 3 4 5'
l2 = s.split(" ")
print(l2)
l2.reverse()
print(l2)

# for i in l2:
#     print(i)
