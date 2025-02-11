import numpy as np
import matplotlib.pyplot as plt

# Load both sensor data files into their respective variables
backLegSensorValues = np.load("data/backLegSensorValuesData.npy")
frontLegSensorValues = np.load("data/frontLegSensorValuesData.npy")

# Plot the back leg sensor values (with wider line)
plt.plot(backLegSensorValues, label="Back Leg", linewidth=2)

# Plot the front leg sensor values (with default line width)
plt.plot(frontLegSensorValues, label="Front Leg", linewidth=2)

# Add titles and labels to the plot
plt.title("Touch Sensor Values Over Time")
plt.xlabel("Time Steps")
plt.ylabel("Sensor Value")

# Add a legend to differentiate between the sensors
plt.legend()

# Show the plot
plt.show()
