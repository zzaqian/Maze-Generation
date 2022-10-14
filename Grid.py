from Cell import *
import numpy as np
import random

import pygame
from pygame.locals import *

class Grid():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.grid = self.prepareGrid()
        self.configureCells()

    def prepareGrid(self):
        arr = np.empty((self.rows, self.cols), dtype=Cell)
        for row in range(self.rows):
            for col in range(self.cols):
                arr[row,col] = Cell(row, col)
        return arr

    def configureCells(self):
        for cell in self.eachCell():
            row, col = cell.row, cell.col
            cell.north = self.access(row-1, col)
            cell.south = self.access(row+1, col)
            cell.east = self.access(row, col+1)
            cell.west = self.access(row, col-1)

    def access(self, row, col):
        if row < 0 or row > self.rows-1:
            return None
        if col < 0 or col > self.cols-1:
            return None
        return self.grid[row, col]

    def randomCell(self):
        row = random.choice(range(self.rows))
        col = random.choice(range(self.cols))
        return self.access(row, col)

    def size(self):
        return self.rows * self.cols

    def eachRow(self):
        for row in self.grid:
            yield row

    def eachCell(self):
        for row in self.eachRow():
            for cell in row:
                if cell:
                    yield cell

    def contentsOf(self, cell):
        return " "

    def backgroundColorFor(self, cell):
        return None

    def toString(self):
        output = "+" + "---+" * self.cols + "\n"

        for row in self.eachRow():
            top = "|"
            bottom = "+"

            for cell in row:
                if cell:
                    pass
                else:
                    cell = Cell(-1, -1)
                
                body = " {} ".format(self.contentsOf(cell))
                eastBoundary = " " if cell.isLinked(cell.east) else "|"
                top += body + eastBoundary

                southBoundary = "   " if cell.isLinked(cell.south) else "---"
                corner = "+"
                bottom += southBoundary + corner

            output += top + "\n"
            output += bottom + "\n"

        return output

    def toPNG(self, cellSize=10):
        imgWidth = cellSize * self.cols
        imgHeight = cellSize * self.rows

        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        background = WHITE
        wall = BLACK

        DISPLAYSURF = pygame.Surface((imgWidth+1,imgHeight+1))
        DISPLAYSURF.fill(background)

        backgrounds, walls = 0, 1

        for mode in [backgrounds, walls]:
            for cell in self.eachCell():
                x1 = cell.col * cellSize
                y1 = cell.row * cellSize
                x2 = (cell.col + 1) * cellSize
                y2 = (cell.row + 1) * cellSize

                if mode == backgrounds:
                    color = self.backgroundColorFor(cell)
                    if color: pygame.draw.rect(DISPLAYSURF, color, (x1, y1, cellSize, cellSize))
                else: 
                    if cell.north == None: pygame.draw.line(DISPLAYSURF, wall, (x1, y1), (x2, y1))
                    if cell.west == None: pygame.draw.line(DISPLAYSURF, wall, (x1, y1), (x1, y2)) 

                    if cell.isLinked(cell.east) == False: pygame.draw.line(DISPLAYSURF, wall, (x2, y1), (x2, y2))
                    if cell.isLinked(cell.south) == False: pygame.draw.line(DISPLAYSURF, wall, (x1, y2), (x2, y2))

        return DISPLAYSURF

    def deadends(self):
        arr = np.array([]) 

        for cell in self.eachCell():
            if len(cell.links) == 1: arr = np.append(arr, [cell]) 

        return arr

    def solve_depthFirst(self, start, goal):
        stack = list() 
        stack.append(start) 
        start.isVisited = True

        while not goal.isVisited:
            current = stack[-1]
            neighbors = list()
            for neighbor in current.links.keys():
                if not neighbor.isVisited: neighbors.append(neighbor)

            if len(neighbors) == 0:
                stack.pop(-1) 
            else:
                neighbor = random.choice(neighbors) 
                stack.append(neighbor) 
                neighbor.isVisited = True 

        return stack
