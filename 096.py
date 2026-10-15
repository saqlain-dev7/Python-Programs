# Reverse number triangle: row starts from row number and counts down to 1
n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    print("".join(str(j) for j in range(i, 0, -1)))
