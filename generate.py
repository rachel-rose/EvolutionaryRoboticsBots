import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x= 0
y = 0
z = 0.5

length2 = 1
width2 = 1
height2 = 1
x2= .9
y2 = 0
z2 = 1.5

# Number of towers and height of each tower
num_towers = 5
tower_height = 10
box_num = 0

for k in range(tower_height):
    # Send the cube at the calculated position with the specified size
    pyrosim.Send_Cube(name=f"Box_{box_num}", pos=[x, y, z], size=[length, width, height])
            
    # Update the position for the next block (on top of the previous one)
    z += height  # The new block will be placed directly above the previous one
            
    # Reduce the size of the next block by 10%
    length *= 0.9
    width *= 0.9
    height *= 0.9

    box_num += box_num

pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])
pyrosim.Send_Cube(name="Box2", pos=[x2, y2, z2] , size=[length2, width2, height2])
pyrosim.End()