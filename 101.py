# Right-aligned alphabet triangle
n = int(input("Enter number of rows (1-26): "))
for i in range(1, min(n, 26) + 1):
    print(" " * (n - i) + "".join(chr(65 + j) for j in range(i)))
