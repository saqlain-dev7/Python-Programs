# Count set bits
n = int(input("Enter a non-negative integer: "))
count = 0
while n > 0:
    count += n & 1
    n >>= 1
print("Number of set bits:", count)
