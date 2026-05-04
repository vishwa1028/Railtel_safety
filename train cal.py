# Get initial speed from user input
initial_speed_kmh = int(input("Enter the speed in km/h: "))

# Constants
deceleration = 0.8  # deceleration in m/s^2

# Convert initial speed to m/s
initial_speed_ms = (initial_speed_kmh * 1000) / 3600

# Calculate stopping distance
stopping_distance = (0 - initial_speed_ms**2) / (2 * deceleration)

# Calculate time to stop
time_to_stop = stopping_distance / abs(deceleration)

# Output results
print(f"Initial Speed: {initial_speed_kmh} km/h")
print(f"Stopping Distance: {stopping_distance:.2f} meters")
print(f"Time to Stop: {time_to_stop:.2f} seconds")
