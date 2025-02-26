'''
class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()

'''
import pybullet as p
import pybullet_data
import constants as c
from robot import ROBOT
from world import WORLD
import time

class SIMULATION:
    def __init__(self):
        # Connect to PyBullet
        self.physicsClient = p.connect(p.GUI)

        # Set additional search path for PyBullet data
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # Configure the visualizer
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)

        # Set gravity in the simulation
        p.setGravity(0, 0, c.GRAVITY, self.physicsClient)

        # Create world and robot instances
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        # Run the simulation loop
        for i in range(c.ITERATIONS):
            print(i)
            
            p.stepSimulation()

            '''
            # Read sensor values
            backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            print("backleg sensor value: ", backLegSensorValues[i])
            
            frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            print("frontleg sensor value: ", frontLegSensorValues[i])

            # Set motor commands
            pyrosim.Set_Motor_For_Joint(
                bodyIndex=sim.robot.robotId,  #added acess to robotId from robot
                jointName=b'Torso_BackLeg',
                controlMode=p.POSITION_CONTROL,
                targetPosition=targetAngles[i],
                maxForce=c.MAX_FORCE
            )

            pyrosim.Set_Motor_For_Joint(
                bodyIndex=sim.robot.robotId, #added acess to robotId from robot
                jointName=b'Torso_FrontLeg',
                controlMode=p.POSITION_CONTROL,
                targetPosition=targetAngles2[i],
                maxForce=c.MAX_FORCE
            )
            '''

            time.sleep(c.TIME_STEP)
            