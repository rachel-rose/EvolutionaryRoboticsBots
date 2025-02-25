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
