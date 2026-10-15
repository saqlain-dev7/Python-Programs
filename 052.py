# Happy number
n = int(input("Enter a positive integer: "))
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    n = total
print("Happy number" if n == 1 else "Not a happy number")
