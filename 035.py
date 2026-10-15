# Alphabet, digit, or special character
ch = input("Enter one character: ")
if len(ch) != 1:
    print("Enter exactly one character")
elif ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")
