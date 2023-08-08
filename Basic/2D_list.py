
number = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
        
print (number[0][0])
print (number[3][0])

for row in number : 
    print(row)

print("\n*********************\n")

for row in number :
    for col in row :
        print (col)
