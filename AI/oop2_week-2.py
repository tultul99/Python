number = int(input('Enter a number: '))
print(f"Square of {number} is {pow(number,2)}")


def find_F(f):
    c = ((f-32)*5)/9
    return c

f = float(input('Enter value in celsius: '))
print(f'Fahrenheit value is {find_F(f)}')



n = int(input('Enter a number: '))
print(f"{n} square is {n*n}")

def celcius(c):
    f = ((c*9)/5)+32
    print(f'Temperature in Fahrenheit is {f}')

c = float(input('Enter temperature in Celsius: '))
celcius(c)