# Heart shape pattern (approximate using a common star pattern)
for row in range(6):
    line = ""
    for col in range(7):
        if (row == 0 and col in (1, 2, 4, 5)) or (row == 1 and col in (0, 1, 2, 3, 4, 5, 6)) or (row == 2 and col in (0, 1, 2, 3, 4, 5, 6)) or (row == 3 and col in (1, 2, 3, 4, 5)) or (row == 4 and col in (2, 3, 4)) or (row == 5 and col == 3):
            line += "*"
        else:
            line += " "
    print(line.rstrip())
