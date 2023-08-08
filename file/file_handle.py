
# file = open("queen.txt", "r")  # read

# print(file.readable())
# print (file.read())
# print (file.readline())
# print (file.readlines()[2])

# for name in file.readlines() :           #  ['a','b']
#     print (name)

# file.close()





# f = open("Asme.txt", "w")  # write
# # f.write ("<p>This is HTML</p>")
# f.write ("A - Asme")
# f.write ("\nT - Tultul")
# f.write ("\nT - believe")
# f.close()





# file = open("queen.txt", "a")  # append
# file.write ("\nS - Samsun")
# file.write ("\nN - Naher")
# file.write ("\nA - Asme")
# file.close()






# f = open('reading_file.txt','a')
# f.close()

f = open("reading_file.txt", "r+")  # reading + writing

# f.write('Look ar the sky')
# f.write('\nLets fly out')

print(f.read())

f.close()
