# Convert Celsius to Fahrenheit and Fahrenheit to Celsius
choice = input("Enter C to convert Celsius to Fahrenheit, or F for Fahrenheit to Celsius: ").upper()
if choice == "C":
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", (c * 9 / 5) + 32)
elif choice == "F":
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius:", (f - 32) * 5 / 9)
else:
    print("Invalid choice.")
