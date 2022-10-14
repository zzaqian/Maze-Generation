from math import cos, sin, pi
from Grid import * 
from PolarCell import * 

class PolarGrid(Grid):
    def __init__(self, rows):
        super().__init__(rows, 1) 

    def prepareGrid(self):
        rows = list()
        rows.append(np.array([PolarCell(0, 0)]))

        rowHeight = 1 / self.rows 

        for row in np.arange(1, self.rows):
            radius = row / self.rows 
            circum = 2 * pi * radius 

            previousCount = len(rows[row-1]) 
            estimatedCellWidth = circum / previousCount 
            ratio = round(estimatedCellWidth / rowHeight) 

            cells = previousCount * ratio 
            currentRow = np.array([])
            for col in range(cells): 
                currentRow = np.append(currentRow, PolarCell(row, col))
            rows.append(currentRow)

        return rows
    
    def configureCells(self):
        for cell in self.eachCell():
            row = cell.row
            col = cell.col 
            if row > 0:
                cell.cw = self.access(row, col+1)
                cell.ccw = self.access(row, col-1) 

                ratio = len(self.grid[row]) / len(self.grid[row-1]) 
                parent = self.access(row-1, int(col/ratio))
                parent.outward = np.append(parent.outward, [cell]) 
                cell.inward = parent

    def access(self, row, col):
        if row < 0 or row > self.rows-1:
            return None
        #if col < 0 or col > len(self.grid[row])-1:
         #   return None
        #return self.grid[row][col]
        return self.grid[row][col % len(self.grid[row])] # use modulus to make the first cell and the last cell of a row adjacent.

    def randomCell(self):
        row = random.choice(range(self.rows))
        col = random.choice(range(len(self.grid[row])))
        
        return self.access(row, col)

    def toPNG(self, cellSize=30):
        imgSize = 2 * self.rows * cellSize 
        
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        background = WHITE
        wall = BLACK

        DISPLAYSURF = pygame.Surface((imgSize+1,imgSize+1))
        DISPLAYSURF.fill(background) 

        center = imgSize / 2

        for cell in self.eachCell():
            if cell.row == 0:
                continue

            theta = 2 * pi / len(self.grid[cell.row]) 
            innerR = cell.row * cellSize 
            outerR = (cell.row + 1) * cellSize 
            thetaCcw = cell.col * theta 
            thetaCw = (cell.col + 1) * theta 

            ax = center + int((innerR * cos(thetaCcw))) 
            ay = center + int((innerR * sin(thetaCcw))) 
            bx = center + int((outerR * cos(thetaCcw))) 
            by = center + int((outerR * sin(thetaCcw))) 
            cx = center + int((innerR * cos(thetaCw))) 
            cy = center + int((innerR * sin(thetaCw))) 
            dx = center + int((outerR * cos(thetaCw))) 
            dy = center + int((outerR * sin(thetaCw))) 

            rect = Rect(center - innerR, center - innerR, 2*innerR, 2*innerR)
            if cell.isLinked(cell.inward) == False: pygame.draw.arc(DISPLAYSURF, wall, rect, -thetaCw, -thetaCcw) # Cao ni ma pygame de jiaodu shi zhengzhe zhuan de
            if cell.isLinked(cell.cw) == False: pygame.draw.line(DISPLAYSURF, wall, (cx, cy), (dx, dy)) 

        pygame.draw.circle(DISPLAYSURF, wall, (center, center), self.rows * cellSize, width=1) 

        return DISPLAYSURF