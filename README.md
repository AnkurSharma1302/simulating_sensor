# Washing Machine Temperature Monitoring

This project simulates monitoring the internal temperature of a washing machine during a wash cycle. The collected temperature data is analyzed, visualized, and checked for overheating issues, with the option to replace simulated data with real-time sensor data for real-world applications.

---

## Features

1. **Data Simulation**:
   - The internal temperature of the washing machine during a 60-minute wash cycle is simulated using random values between 30°C and 90°C.
   - Temperatures represent a range from a cold wash (30°C) to a hot wash (90°C).

2. **Data Storage**:
   - Temperature readings are stored in a CSV file (`temperature_readings.csv`) with two columns:
     - **Minute**: The time in minutes (1 to 60).
     - **Temperature (Celsius)**: The temperature at each minute.

3. **Data Visualization**:
   - A line chart is generated using `matplotlib` to display the variation of temperature over time.
   - Overheating events (temperatures > 80°C) are highlighted with red markers on the chart.
   - A threshold line at 80°C is displayed to identify overheating points.

4. **Real-World Applications**:
   - The simulated random temperature data can be replaced with real-time sensor data for monitoring actual washing machines.

## Real-World Applications
In a real-life scenario, the random temperature data can be replaced with real-time sensor data collected from a washing machine. The workflow remains the same:

1. Collect temperature readings from the sensor.
2. Store the readings in a CSV file.
3. Use the analysis and visualization scripts to monitor and analyze the temperature data.

## Libraries Used
1. pandas: For data manipulation and reading/writing CSV files.
2. matplotlib: For creating line charts to visualize temperature trends.
3. random: To simulate random temperature values for the wash cycle

## Example Output
### Simulated Data Visualization
1. Blue Line: Temperature over time.
2. Red Points: Overheating values (temperatures > 80°C).
3. Orange Dashed Line: Overheating threshold at 80°C.

![image](https://github.com/user-attachments/assets/b0aa521b-60ee-4f21-980c-3c6f3c86d2ac)

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it for your applications.

