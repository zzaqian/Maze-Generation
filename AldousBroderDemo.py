from Grid import *
from AldousBroder import *

grid = Grid(20, 20)
AldousBroder.on(grid) 

filename = "aldous_broder.png"
pygame.image.save(grid.toPNG(), filename) 
print("saved to {}".format(filename))