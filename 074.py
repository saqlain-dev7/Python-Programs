# Approximate sin(x) series: x - x^3/3! + x^5/5! - ...
import math
x = float(input("Enter x in radians: "))
terms = int(input("Enter number of terms: "))
total = 0.0
for i in range(terms):
    power = 2 * i + 1
    factorial = 1
    for j in range(1, power + 1):
        factorial *= j
    term = (x ** power) / factorial
    if i % 2 == 0:
        total += term
    else:
        total -= term
print("Series sum:", total)
print("math.sin(x) for comparison:", math.sin(x))
