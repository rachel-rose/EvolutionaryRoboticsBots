'''
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
'''
import numpy as numpy
import matplotlib.pyplot as plt

# backLegSensorValues = numpy.load("data/back_leg_sensor_values.npy")
# frontLegSensorValues = numpy.load("data/front_leg_sensor_values.npy")

# plt.plot(backLegSensorValues, label="back Leg sensor values", linewidth=3)
# plt.plot(frontLegSensorValues, label="front Leg sensor values")
# plt.title("Back leg and front leg sensor values")
# plt.legend()
# plt.savefig("plot.png", dpi=300, bbox_inches='tight')
# plt.show()

# Load motor target angles from file
targetAngles = numpy.loadtxt("data/target_angles.txt")

# Create a time axis (same length as targetAngles)
time_steps = numpy.linspace(0, 2 * numpy.pi, len(targetAngles))

# Plot the sinusoidal motor target angles
plt.plot(time_steps, targetAngles, label="Motor Target Angles", linewidth=3)

# Formatting the plot
plt.xlabel("Time Steps")
plt.ylabel("Target Angle (radians)")
plt.title("Sinusoidal Motor Target Angles")
plt.legend()
plt.grid(True)

# Save and display the plot
plt.savefig("motor_plot.png", dpi=300, bbox_inches='tight')
plt.show()