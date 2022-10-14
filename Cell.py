from Distances import *
import numpy as np

class Cell():
    def __init__(self, row, col):
        self.row = row
        self.col = col # position
        self.links = dict()
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.isVisited = None

    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)
        return self

    def unlink(self, cell, bidi=True):
        self.links.pop(cell)
        if bidi:
            cell.unlink(self, False)
        return self

    def getLinks(self):
        return self.links.keys()

    def isLinked(self, cell):
        if cell in self.links:
            return True
        return False

    def neighbors(self):
        l = np.array([])
        if self.north: 
            #for i in range(2):
                l = np.append(l, [self.north])
        if self.south: 
            #for i in range(2):
                l = np.append(l, [self.south])
        if self.east: 
            #for i in range(3):
                l = np.append(l, [self.east])
        if self.west: 
            #for i in range(3):
                l = np.append(l, [self.west])
        
        return l

    def distances(self):
        distances = Distances(self)
        frontier = np.array([self]) 

        while frontier.size != 0: 
            newFrontier = np.array([]) 

            for cell in frontier:
                for linked in cell.links:
                    if linked not in distances.cells: # don't use the textbook's getvalue method
                        distances.set(linked, distances.get(cell) + 1)
                        newFrontier = np.append(newFrontier, [linked]) 

            frontier = np.copy(newFrontier)

        return distances

