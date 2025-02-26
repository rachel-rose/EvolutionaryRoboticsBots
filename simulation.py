import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import random
import math
import constants as c
from robot import ROBOT
from world import WORLD
from motor import MOTOR

class SIMULATION:
    
    def __init__(self):
        print("Connecting to PyBullet...")  # Debugging line

        # test- Connect to PyBullet before loading anything
        self.physicsClient = p.connect(p.GUI)  # Keep method header unchanged

        # test- Set additional search path for PyBullet data
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # test- Configure PyBullet settings
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)

        # test- Set gravity
        p.setGravity(0, 0, c.GRAVITY)

        print("Simulation initialized successfully!")  # Debugging line
        self.world = WORLD()
        self.robot = ROBOT()
    
        print("Simulation initialized successfully!")  # Debugging line




    def Run(self):
        
        for t in range(c.ITERATIONS):
            self.robot.Sense(t)
            self.robot.Act(t)
            p.stepSimulation()
           
            time.sleep(c.TIME_STEP)

            print("Iteration: ", t)

        self.Save_Data()

    def Save_Data(self):
        numpy.save("data/back_leg_sensor_values.npy", self.backLegSensorValues)
        numpy.save("data/front_leg_sensor_values.npy", self.frontLegSensorValues)

    def __del__(self):
        p.disconnect()