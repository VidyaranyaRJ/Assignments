def analyze_temperatures(temperature_readings):
    avg_temp = sum(temperature_readings) / len(temperature_readings)
    highest_temp = max(temperature_readings)
    lowest_temp = min(temperature_readings)
    return avg_temp, highest_temp, lowest_temp

# Sample Input
temperature_readings = [25, 28, 21, 24, 27]
avg, highest, lowest = analyze_temperatures(temperature_readings)
print(f"Average Temperature: {avg}")
print(f"Highest Temperature: {highest}")
print(f"Lowest Temperature: {lowest}")
