# GCD / HCF of two numbers
a = abs(int(input("Enter first integer: ")))
b = abs(int(input("Enter second integer: ")))
while b != 0:
    a, b = b, a % b
print("GCD / HCF:", a)
