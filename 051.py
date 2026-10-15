# Check if a number is a palindrome
n = int(input("Enter a non-negative integer: "))
original = n
reverse = 0
while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10
if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
