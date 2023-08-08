'''
name = "Samsun Naher Asme"
id = "203-15-3882"
department = "CSE"
email = "naher15-3882@diu.edu.bd"
print(name)
print(id)
print(department)
print(email)


for i in range(8):
    id = input("Enter student roll number: ")
    total = 0.0

    for j in range(3):
        num = int(input(f'Enter {j + 1} no subject marks: '))
        total =+ num
    
    print(f'{i + 1} no student roll no: {id}\
    average marks: {total / 3} ')
'''

print(f'Md. Rakibul Islam Shanto\n\
id: 203-15-3871\n\
Department: CSE\n\
email: rakibul15-3871@diu.edu.bd\n')


for index in range(0, 8):
    roll = input(f"Enter {index + 1} student roll number = ")
    t = 0.0

    for value in range(0, 3):
        num = int(input(f'{value + 1} no subject marks = '))
        t =+ num
    
    print(f'{index+1} student roll -> {roll}\n')
    print(f'average marks -> {t/3} ')
