from Grid import *
from RecursiveBacktracker import *

grid = Grid(20, 20)
#start = grid.randomCell()
#RecursiveBacktracker.onRecursion(grid, start)
RecursiveBacktracker.on(grid)

filename = "recursive_backtracker.png"
pygame.image.save(grid.toPNG(), filename) 
print("saved to {}".format(filename))