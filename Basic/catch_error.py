
# value = 10/0

try :
    n = int(input("Enter a number: "))
    print (n)
    
    value = 10/0

except ZeroDivisionError as err:
    print(err)
    # print ("Divided by zero")
    
except ValueError :
    print ("Invalid input!")

except Exception as asme:
    print(asme)
    # print ("All type of error")
