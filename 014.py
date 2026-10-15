# Check whether the Kth bit is set (bit positions start at 0 from the right)
n = int(input("Enter a non-negative integer: "))
k = int(input("Enter bit position K (starting from 0): "))
if n & (1 << k):
    print("Kth bit is set")
else:
    print("Kth bit is not set")
