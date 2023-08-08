ss = "Rakibul Islam"

print (ss.upper())
print (ss.isupper())
print (ss.lower())
print (ss.lower().islower())

ss = "shanto"
print (ss, "is lower? ->" , ss.islower())

ss = "Rakibul Islam Shanto"
print (len(ss))   #length

print (ss[0])         #index
print (ss.index("R"))  # search by character

print (ss[4])
print (ss.index("b"))

print (ss.index("Sha"))   #will show the starting ch index

print (ss.replace("Shanto", "SHANTO"))

ss = "shanto"
print (ss.isalpha())