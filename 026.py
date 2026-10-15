# Day of week from number
days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday",
        5: "Friday", 6: "Saturday", 7: "Sunday"}
n = int(input("Enter a number (1-7): "))
if n in days:
    print(days[n])
else:
    print("Invalid day number")
