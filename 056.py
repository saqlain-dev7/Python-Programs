# Check if a number is prime
n = int(input("Enter an integer: "))
is_prime = n >= 2
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not prime")
