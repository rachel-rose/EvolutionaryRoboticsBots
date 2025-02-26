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
        self.motors= {}

    def Prepare_To_Sense(self):
        self.sensors = {}
        #for linkName in pyrosim.linkNamesToIndices:
            #print("this is "+ "" + linkName)
        # Debugging: Check if pyrosim.linkNamesToIndices is populated
        print("Checking linkNamesToIndices...")  
        if hasattr(pyrosim, "linkNamesToIndices"):
            print("Link Names to Indices:", pyrosim.linkNamesToIndices)  # Print dictionary
        
            # Iterate through the links and print their names
            for linkName in pyrosim.linkNamesToIndices:
                print("this is " + linkName)  # Expected output: 3 names
                self.sensors[linkName] = None  # Store sensors for each link
        
        else:
            print("ERROR: linkNamesToIndices is not defined. Check if Prepare_To_Simulate() is working.")
    
