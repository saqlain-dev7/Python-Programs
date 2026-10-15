# Zigzag pattern (three rows)
n = int(input("Enter number of columns (at least 3): "))
for r in range(3):
    line = ""
    for c in range(n):
        if (r == 0 or r == 2) and c % 4 == 0:
            line += "*"
        elif r == 1 and c % 2 == 0:
            line += "*"
        else:
            line += " "
    print(line.rstrip())
