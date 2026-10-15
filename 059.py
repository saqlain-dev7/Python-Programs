# LCM of two numbers
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
x, y = abs(a), abs(b)
while y != 0:
    x, y = y, x % y
gcd = x
if a == 0 or b == 0:
    lcm = 0
else:
    lcm = abs(a * b) // gcd
print("LCM:", lcm)
