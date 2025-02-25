'''class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors= {}
        pass
'''

import pybullet as p
import pyrosim.pyrosim as pyrosim

class ROBOT:
    def __init__(self):
        # Load the robot model
        self.robotId = p.loadURDF("body.urdf")

        # Prepare for simulation
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.sensors = {}
        self.motors= {}
