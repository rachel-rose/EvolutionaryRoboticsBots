import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy as numpy

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

for i in range(1000):
    p.stepSimulation()
    #print(f"interation num: {i}")
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    #print(f"backleg is: {backLegTouch}")
    time.sleep(1/60)

p.disconnect()

#print new var
print(f"backleg is: {backLegSensorValues}")