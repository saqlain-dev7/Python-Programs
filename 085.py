# Hollow rectangle of stars
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
for r in range(rows):
    line = ""
    for c in range(cols):
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            line += "*"
        else:
            line += " "
    print(line)
