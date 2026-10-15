# Salary with overtime paid at 1.5 times the hourly rate after 40 hours
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
if hours <= 40:
    salary = hours * rate
else:
    salary = 40 * rate + (hours - 40) * rate * 1.5
print("Salary:", salary)
