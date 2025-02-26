import pybullet as p
import pyrosim.pyrosim as pyrosim

class WORLD:
    def __init__(self):
        # Load the ground plane
        self.planeId = p.loadURDF("plane.urdf")

        # Load additional world objects
        p.loadSDF("world.sdf")