from Grid import *
from HuntAndKill import *

grid = Grid(20, 20)
HuntAndKill.on(grid) 

filename = "hunt_and_kill.png"
pygame.image.save(grid.toPNG(), filename) 
print("saved to {}".format(filename))