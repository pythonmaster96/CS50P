# Challenge 07 - Tip Calculator
# Goal: Calculate tip amount and total bill

bill = float(input("How much is the bill? "))
tip_percent = int(input("How much is the tip? "))
tip = tip_percent / 100 * bill
total = bill + tip
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")
