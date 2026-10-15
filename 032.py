# Check sign, and if positive check even or odd
n = int(input("Enter an integer: "))
if n > 0:
    print("Positive")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
elif n < 0:
    print("Negative")
else:
    print("Zero")
