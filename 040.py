# ATM withdrawal; sample minimum balance rule: keep at least 500
balance = float(input("Enter current balance: "))
amount = float(input("Enter withdrawal amount: "))
minimum_balance = 500
if amount <= 0:
    print("Invalid withdrawal amount")
elif amount > balance:
    print("Rejected: insufficient balance")
elif balance - amount < minimum_balance:
    print("Rejected: minimum balance of", minimum_balance, "must remain")
else:
    print("Approved. Remaining balance:", balance - amount)
