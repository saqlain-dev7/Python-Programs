# Number diamond: 1, 121, 12321, ...
n = int(input("Enter half-height: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)) + "".join(str(j) for j in range(i - 1, 0, -1)))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)) + "".join(str(j) for j in range(i - 1, 0, -1)))
