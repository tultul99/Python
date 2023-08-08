co_ordinates = (4,5)    # can't change/erase/add...
# co_ordinates[1] = 7
print (co_ordinates[0])
print (co_ordinates[1])

coor = [(1,2),(3,4),(5,6)] 

#### difference between list & tuples

# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)

# elements 2nd to 4th
print(my_tuple[1:4])

# elements beginning to 2nd
print(my_tuple[:-6])

# elements 7th to end
print(my_tuple[6:])

# elements beginning to end
print(my_tuple[:])

# print(type(my_tuple))