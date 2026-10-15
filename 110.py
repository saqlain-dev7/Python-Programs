# Plus (+) pattern
n = int(input("Enter an odd size for the plus sign: "))
middle = n // 2
for i in range(n):
    line = ""
    for j in range(n):
        if i == middle or j == middle:
            line += "*"
        else:
            line += " "
    print(line)
