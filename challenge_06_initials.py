# Challenge 06 - Initials Generator
# Goal: Print initials from first, middle, and last name

first = input("What is your first name? ")
middle = input("What is your middle name? ")
last = input("What is your last name? ")
print(f"{first[0].upper()}.{middle[0].upper()}.{last[0].upper()}.")
