name = input ("Ener your name: ")
# age = input("Enter your age: ")
# print ("your name:", name, "\nyour age:" ,age)

birth_year = input ("Enter your birth year: ")
# age = 2022- birth_year  # won't gonna work
age = 2022 - int(birth_year)
print ("Hello", name , ",you are", age, "year's old.")
# print ("Calculated age: " + str(age))

print ("####################  Mad Libs  ####################")

name = input ("Enter your name: ")
number = input ("Enter a number: ")
color = input ("Enter a color name: ")

print ("Hi "+name+", you are a good person.")
print ("Is "+number+" your favourite number?")
print ("I love to wear "+color+" dresses.")


a,b = input("Enter a number: "), input()
