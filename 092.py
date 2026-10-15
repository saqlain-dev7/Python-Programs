# Pascal's triangle
n = int(input("Enter number of rows: "))
row = [1]
for i in range(n):
    print(" " * (n - i - 1), end="")
    print(*row)
    next_row = [1]
    for j in range(len(row) - 1):
        next_row.append(row[j] + row[j + 1])
    next_row.append(1)
    row = next_row
