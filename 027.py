# Electricity bill using sample slab rates (rates were not specified in the question)
units = float(input("Enter electricity units used: "))
if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2.5
elif units <= 300:
    bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
else:
    bill = 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 6
print("Bill amount:", bill if units >= 0 else "not calculated")
