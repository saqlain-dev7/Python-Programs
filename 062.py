# Compute 1 - 2 + 3 - 4 + ... up to N terms
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total -= i
    else:
        total += i
print("Sum:", total)
