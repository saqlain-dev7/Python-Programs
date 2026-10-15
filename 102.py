# Centered alphabet pyramid: A, ABA, ABCBA, ...
n = int(input("Enter number of rows (1-26): "))
for i in range(1, min(n, 26) + 1):
    left = "".join(chr(65 + j) for j in range(i))
    right = "".join(chr(65 + j) for j in range(i - 2, -1, -1))
    print(" " * (n - i) + left + right)
