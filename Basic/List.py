color = ["blue", "white", "black", "green"]

print (color)
print (color[0] + " = " + color[-3])
print (color[1] + " = " + color[-2])   # negative for backward
print (color[2] + " = " + color[-1])

print (color[2: ])   # 2 to ->
print (color[1:3])   # range  1 -> 2

number = [2, 4, 7, 9, 7, 12, 19]
# color.extend(number)
# print (color)

color.append("Queen")
print (color)

color.insert(2, "RED")
print (color)

color.remove("RED")
print (color)

color.pop()
print (color)

# color.clear()
# print(color)

print (color.index("white"))

print (number.count(7))

number.sort()
print(number)

number.reverse()
print(number)

name = color.copy()
print (name)
