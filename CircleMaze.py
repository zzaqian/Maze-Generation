from PolarGrid import * 
from RecursiveBacktracker import * 

grid = PolarGrid(20) 
RecursiveBacktracker.on(grid) 

filename = "circle_maze.png" 
pygame.image.save(grid.toPNG(50), filename) 
print("saved to {}".format(filename))