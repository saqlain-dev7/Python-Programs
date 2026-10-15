# Right arrow pattern
n = int(input("Enter number of rows in upper half: "))
for i in range(1, n + 1):
    print("*" + " " * (2 * i - 1) + "*" * i)
for i in range(n - 1, 0, -1):
    print("*" + " " * (2 * i - 1) + "*" * i)
