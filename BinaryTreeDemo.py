from Grid import *
from BinaryTree import *

grid = Grid(40,40)
BinaryTree.on(grid)
print(grid.toString())

img = grid.toPNG()
pygame.image.save(img, "maze.png")
