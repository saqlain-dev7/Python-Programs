# Perfect number: sum of proper divisors equals the number
n = int(input("Enter a positive integer: "))
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
print("Perfect number" if n > 0 and total == n else "Not a perfect number")
