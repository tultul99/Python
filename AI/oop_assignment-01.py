E_ID = input("Enter an employee id: ")
workHour = (input("Input total working hour: "))
amount = (input("Input amount per hour: "))

workHour, amount = float(workHour), float(amount)

print("Employee Id =", E_ID)
print("Salary = {:.2f}".format(amount*workHour))
print(f"Salary = {amount*workHour}")
