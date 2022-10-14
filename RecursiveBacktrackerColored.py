from ColoredGrid import *
from RecursiveBacktracker import *

for i in range(6):
    grid = ColoredGrid(100, 100)
    RecursiveBacktracker.on(grid)
    #RecursiveBacktracker.onRecursion(grid, grid.randomCell())  # exceeds python maximum recursion depth (1000)

    middle = grid.access(int(grid.rows/2), int(grid.cols/2))
    grid.setDistances(middle.distances())

    filename = "recursive_backtracker_{}.png".format(i)
    pygame.image.save(grid.toPNG(), filename)
    print("saved to {}".format(filename))