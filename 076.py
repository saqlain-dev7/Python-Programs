# Count vowels in a string using recursion
def count_vowels(text):
    if text == "":
        return 0
    first = 1 if text[0].lower() in "aeiou" else 0
    return first + count_vowels(text[1:])

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))
