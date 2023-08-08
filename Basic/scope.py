s = "Putul"
a = 3882   # global

def Asme () :
    e = 882     # local
    global a
    a = a + 1
    # e += 1
    print(a)
    print(e)

Asme()

for f in range(5):
    print(f)

print(f)

# print(a)