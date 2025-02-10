import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
#p.loadSDF("world.sdf")

robotId = p.loadURDF("body.urdf")
#p.loadSDF("robotId")
p.loadSDF("world.sdf")

for i in range(4000):
    p.stepSimulation()
    print(f"interation num: {i}")
    time.sleep(1/60)

backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

p.disconnect()

