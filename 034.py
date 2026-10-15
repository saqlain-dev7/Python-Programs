# Roots of a quadratic equation ax^2 + bx + c = 0
import math
a = float(input("Enter a (non-zero): "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if a == 0:
    print("Not a quadratic equation because a is zero")
else:
    d = b * b - 4 * a * c
    if d > 0:
        print("Two real roots:", (-b + math.sqrt(d)) / (2 * a), "and", (-b - math.sqrt(d)) / (2 * a))
    elif d == 0:
        print("Equal real roots:", -b / (2 * a))
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-d) / abs(2 * a)
        print("Imaginary roots:", real, "+", imag, "i and", real, "-", imag, "i")
