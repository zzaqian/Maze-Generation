from Mask import * 
from MaskedGrid import * 
from RecursiveBacktracker import * 

mask = Mask.fromPNG("profile_1_100x100.png") 
grid = MaskedGrid(mask) 
RecursiveBacktracker.on(grid) 

filename = "masked_image.png" 
pygame.image.save(grid.toPNG(cellSize = 5), filename) 
print("saved image to {}".format(filename))