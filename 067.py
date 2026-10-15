# Armstrong number for any number of digits
n = int(input("Enter a non-negative integer: "))
digits = str(n)
power = len(digits)
total = 0
for digit in digits:
    total += int(digit) ** power
print("Armstrong number" if total == n else "Not an Armstrong number")
