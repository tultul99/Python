# Format - 1

id = input("Enter an employee id: ")
work_hour = float(input("Input total working hour: "))
salary = float(input("Input amount per hour: "))

print(f"Employee Id = {id}")
print("Salary = {:.2f}".format(salary*work_hour))


# format - 2

E_ID = input("Enter an employee id: ")
workHour = (input("Input total working hour: "))
amount = (input("Input amount per hour: "))

workHour, amount = float(workHour), float(amount)

print("Employee Id =", E_ID)
print("Salary = {:.2f}".format(amount*workHour))
