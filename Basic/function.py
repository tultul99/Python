
def display (name) :
    print(name)
    print ("Welcome.")

def shanto () :
    input ("How are you? : ")

def year (age, b_year) :
    return int(age)+int(b_year)

print ("Hi")

shanto()

display(input("Enter your name: "))

age, birth_year = input("Enter your age: "), input("Enter birth year: ")
print ("Current year:", year(age, birth_year))

print ("Bye")
