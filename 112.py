# Square with diagonals marked
n = int(input("Enter square size (at least 2): "))
for i in range(n):
    line = ""
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or j == n - i - 1:
            line += "*"
        else:
            line += " "
    print(line)
