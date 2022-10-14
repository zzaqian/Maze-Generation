from Grid import * 
import numpy as np 

class MaskedGrid(Grid):
    def __init__(self, mask):
        self.mask = mask 
        super().__init__(self.mask.rows, self.mask.cols) 

    def prepareGrid(self):
        arr = np.empty((self.rows, self.cols), dtype=Cell) 

        for row in range(self.rows):
            for col in range(self.cols):
                if self.mask.get(row, col): arr[row, col] = Cell(row, col) 

        return arr 

    def randomCell(self):
        row, col = self.mask.randomLocation() 
        return self.access(row, col) 

    def size(self):
        return self.mask.count() 