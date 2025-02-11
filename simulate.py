import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import os

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

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
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