# Ticket pricing based on age (sample policy: under 5 free, 5-17 child, 18-59 adult, 60+ senior)
age = int(input("Enter age: "))
if age < 5:
    price = 0
elif age <= 17:
    price = 100
elif age < 60:
    price = 200
else:
    price = 100
print("Ticket price:", price)
