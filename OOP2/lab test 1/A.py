
li = [1,2,3,4,5,6,7,100,110,21,33,32,2,4]

even = []
odd = []
out = []

for index in li:
    if index >= 100:
        out.append(index)
    elif index%2 == 0:
        even.append(index)
    elif index%2 != 0:
        odd.append(index)

print(f"Even number {even}")
print(f"Odd number {odd}")
print(f"Outliners {out}")