
# print ("2^3", 2^3)
print ("2^3", 2**3)

def power (base, power) :
    i = int(power)
    result = 1
    while i != 0 :
        result *= base
        i -= 1
    return result 

a, b = input("Enter base : "), input ("Enter power: ")
print ("Result =",power(int(a), int(b)))

#######################################################

def exponent (base, power) :
    i=0
    result = 1
    while i < power :
        result *= base
        i = i + 1
    return result 

a, b = input("Enter base : "), input ("Enter power: ")
print ("Result =", exponent(int(a), int(b)))

#######################################################

def exponent (base, power) :
    result = 1
    
    for index in range(power) :            # power = 5,    range(power) = 1,2,3,4,5  <- index     
        result *= base
    
    return result 

a, b = input("Enter base : "), input ("Enter power: ")
print ("Result =", exponent(int(a), int(b)))