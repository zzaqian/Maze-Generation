from Grid import *
from SideWinder import *

grid = Grid(40,40)
SideWinder.on(grid)
print(grid.toString())

img = grid.toPNG()
pygame.image.save(img, "maze.png")

deadends = grid.deadends() 
print("{} dead-ends".format(deadends.size))