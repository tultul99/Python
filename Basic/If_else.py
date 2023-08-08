
a, b, c = input(), input(), input()

a = int(a)
b = int(b)
c = int(c)

if a>b and a>c :
    print (a, " is greater.")

elif b>a and b>c :
    print (b, "is greater.")
else :
    print(c, " is greater.")


if a >= 50 or a > 0 :
    print (a, "is a positive number.")

elif a < 0 and not a == 0 :
    print (a, "is a negetive number.")

else :
    print (a, "= Zero")