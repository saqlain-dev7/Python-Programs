# Print each digit from left to right
s = input("Enter a non-negative integer: ").strip()
if s.isdigit():
    for digit in s:
        print(digit)
else:
    print("Please enter a non-negative integer")
