# Swap two integers using XOR
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping: a =", a, ", b =", b)
