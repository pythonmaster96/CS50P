# Challenge 08 - Speed Calculator
# Goal: Calculate average speed using a dedicated function

def calculate_speed(distance, time):
    return distance / time

distance = float(input("Enter distance (km): "))
time = float(input("Enter time (hours): "))
speed = calculate_speed(distance, time)
print(f"Average speed: {speed:.2f} km/h")
