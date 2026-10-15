# Read numbers until -1, then print count and average
count = 0
total = 0
while True:
    n = float(input("Enter a number (-1 to stop): "))
    if n == -1:
        break
    total += n
    count += 1
if count > 0:
    print("Count:", count)
    print("Average:", total / count)
else:
    print("No numbers were entered")
