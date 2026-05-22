# Challenge 03 - Fahrenheit to Celsius Converter
# Goal: Convert a temperature from Fahrenheit to Celsius

fahrenheit = float(input("What is the temperature in Fahrenheit? "))
calculated_celsius = (fahrenheit - 32) * 5 / 9
print(f"{calculated_celsius:.2f}°C")
