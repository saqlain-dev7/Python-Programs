# Alphabet triangle with each row repeating one letter
n = int(input("Enter number of rows (1-26): "))
for i in range(1, min(n, 26) + 1):
    print(chr(64 + i) * i)
