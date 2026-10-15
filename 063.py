# Calculate x^n without using pow()
x = float(input("Enter base x: "))
n = int(input("Enter integer exponent n: "))
if n < 0:
    result = 1
    for _ in range(-n):
        result *= x
    if x == 0:
        print("Undefined for zero raised to a negative power")
    else:
        print("Result:", 1 / result)
else:
    result = 1
    for _ in range(n):
        result *= x
    print("Result:", result)
