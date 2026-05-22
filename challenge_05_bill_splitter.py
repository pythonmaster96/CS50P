# Challenge 05 - Bill Splitter
# Goal: Split a restaurant bill equally among friends

bill = float(input("What is the amount of bill? "))
people = int(input("What is the number of people? "))
print(f"Each person pays: ${bill / people:.2f}")
