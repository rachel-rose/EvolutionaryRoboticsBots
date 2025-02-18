import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import os
import math
import random
import matplotlib.pylab as plt

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
#p.loadSDF("world.sdf")

robotId = p.loadURDF("body.urdf")
#p.loadSDF("robotId")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

# Step 32
# Number of iterations for loop len
num_iterations = 10000 #num_steps
# Create a linearly spaced vector from 0 to 2*pi
x = numpy.linspace(0, 2 * numpy.pi, num_iterations) #time_values
# Generate sinusoidal values, these will range from -1 to 1
targetAngles = numpy.sin(x)

'''
x = numpy.linspace(-numpy.pi, numpy.pi, 201)
plt.plot(x, np.sin(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()'''

# Save the values to a file
numpy.savetxt("targetAngles.txt", targetAngles)

# Plot the values
#plt.plot(x, targetAngles)
plt.plot(numpy.linspace(0, 1000, num_iterations), targetAngles)  # Scaling x-axis to 1000
plt.xlabel("Time Steps")
plt.ylabel("Target Angles")
plt.title("Sinusoidal Target Angles")
plt.grid()
plt.show()

# Exit before entering the loop
exit()

for i in range(num_iterations):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg', 
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.random() * (math.pi/2.0), #-
        maxForce = 500)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg', 
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.random() * (math.pi/2.0), #+
        maxForce = 500)
    time.sleep(1/60)

# Ensure the directory exists before saving
output_dir = "data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save sensor values to a .npy file
numpy.save(os.path.join(output_dir, "backLegSensorValuesData.npy"), backLegSensorValues)
numpy.save(os.path.join(output_dir, "frontLegSensorValuesData.npy"), frontLegSensorValues)

p.disconnect()

#print new var
print(f"backleg is: {backLegSensorValues}")
print(f"Front leg sensor values: {frontLegSensorValues}")