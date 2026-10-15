# Hollow diamond inside a rectangle (simple outline-style version)
n = int(input("Enter half-height: "))
width = 2 * n + 1
for i in range(n + 1):
    left = n - i
    right = n + i
    line = [" "] * width
    if i == 0:
        line[0] = "*"
        line[-1] = "*"
    else:
        line[left] = "*"
        line[right] = "*"
        line[0] = "*"
        line[-1] = "*"
    print("".join(line))
for i in range(n - 1, -1, -1):
    left = n - i
    right = n + i
    line = [" "] * width
    line[left] = "*"
    line[right] = "*"
    line[0] = "*"
    line[-1] = "*"
    print("".join(line))
