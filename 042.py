# Scholarship eligibility (sample criteria; adjust to the institution's rules)
marks = float(input("Enter marks percentage: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))
if marks >= 75 and attendance >= 75 and income <= 250000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
