# Centered number pyramid: 1, 123, 12345, ...
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "".join(str(j) for j in range(1, 2 * i)))
