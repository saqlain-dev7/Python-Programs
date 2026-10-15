# X pattern
n = int(input("Enter an odd size for the X: "))
for i in range(n):
    line = ""
    for j in range(n):
        if j == i or j == n - i - 1:
            line += "*"
        else:
            line += " "
    print(line)
