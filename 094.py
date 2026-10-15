# Inverted number triangle
n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    print("".join(str(j) for j in range(1, i + 1)))
