from Grid import *
from Wilsons import *

grid = Grid(20, 20)
Wilsons.on(grid)

filename = "wilsons.png"
pygame.image.save(grid.toPNG(), filename)
print("saved to {}".format(filename))