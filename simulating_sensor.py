import random
import time
import csv


# Function to generate a random temperature between 30°C and 90°C
def get_temperature():
    return random.uniform(30, 90)

# Simulate a wash cycle
temperature_readings = []
def simulate_wash_cycle():
    
    
    for minute in range(60):  # Simulate for 60 minutes
        temperature = get_temperature()
        temperature_readings.append(temperature)
        time.sleep(1)  # Simulate a delay of 1 second per reading (for real-time simulation, remove this)
        print(f"Minute {minute + 1}: Temperature = {temperature:.2f}°C")
    
    return temperature_readings

# Run the simulation
if __name__ == "__main__":
    readings = simulate_wash_cycle()
    print("\nTemperature readings during the wash cycle:")
    print(readings)

def analyze_data(data):
    # Calculate the average temperature
    average_temperature = sum(data) / len(data)
    
    # Check for readings exceeding the threshold of 80°C
    overheating_issues = [temp for temp in data if temp > 80]
    
    # Display analysis results
    print(f"Average Temperature: {average_temperature:.2f}°C")
    
    if overheating_issues:
        print(f"Overheating detected! Temperatures exceeding 80°C: {overheating_issues}")
    else:
        print("No overheating issues detected.")

# Example usage
if __name__ == "__main__": # Replace with actual readings if available
    
    # Analyze the data
    analyze_data(temperature_readings)



def export_to_csv(data):
    # Export temperature readings to a CSV file
    with open("temperature_readings.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Minute", "Temperature (°C)"])  # Header
        for minute, temperature in enumerate(data, start=1):
            writer.writerow([minute, temperature])
    print("Data exported to 'temperature_readings.csv' successfully!")

# Example usage
if __name__ == "__main__":
    # Export the data to CSV
    export_to_csv(temperature_readings)

