import pyrosim.pyrosim as pyrosim
'''
pyrosim.Start_SDF("world.sdf")

length = 1
width = 1
height = 1
x= 0
y = 0
z = 0.5

# Number of towers and height of each tower
num_rows = 5
num_cols = 5
tower_height = 10
box_num = 0

for i in range(num_cols):
    for j in range(num_rows):
        for k in range(tower_height):
            # Send the cube at the calculated position with the specified size
            pyrosim.Send_Cube(name=f"Box_{box_num}", pos=[x, y, z], size=[length, width, height])
                    
            # Update the position for the next block (on top of the previous one)
            z += height  # The new block will be placed directly above the previous one
                    
            # Reduce the size of the next block by 10%
            length *= 0.9
            width *= 0.9
            height *= 0.9

            box_num += 1
        #reset base box dimensions
        length = 1
        width = 1
        height = 1
        x= 0 + j
        y = 0 + i
        z = 0.5
'''

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[5, 0, 0.5] , size=[1, 1, 1])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 0.5] , size=[1, 1, 1])
    pyrosim.Send_Joint( name = "Torso_Leg" , parent= "Torso" , child = "Leg" , type = "revolute", position = [0.5, 0, 1])
    pyrosim.Send_Cube(name="Leg", pos=[1.0,0,1.5] , size=[1, 1, 1])
    pyrosim.End()


Create_World()
Create_Robot()