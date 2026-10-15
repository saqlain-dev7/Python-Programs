# Classify a character
ch = input("Enter one character: ")
if len(ch) != 1:
    print("Please enter exactly one character")
elif ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")
