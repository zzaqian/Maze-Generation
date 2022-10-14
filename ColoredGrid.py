from Grid import *

class ColoredGrid(Grid):
    def setDistances(self, distances):
        self.distances = distances 
        farthest, self.maximum = distances.max()

        self.breadcrumbs = None # just to initialze breadcrumbs

    def setSolution_Dijkstra(self, goal):
        self.breadcrumbs = self.distances.pathTo(goal) 

    def setSolution_depthFirst(self, start, goal):
        self.breadcrumbs = self.solve_depthFirst(start, goal)

    def backgroundColorFor(self, cell):
        if cell in self.distances.cells: # since we don't check if self.distances exists, using ColoredGrid requires that we call the setDistances function
            distance = self.distances.get(cell)
        else:
            return None

        intensity = 1 - distance / self.maximum 
        dark = round(255 * intensity)
        bright = 128 + round(127 * intensity) 
        if self.breadcrumbs: 
            if isinstance(self.breadcrumbs, Distances):
                if cell in self.breadcrumbs.cells:
                    return (bright, bright, dark) # produces yellow
            elif isinstance(self.breadcrumbs, list):
                if cell in self.breadcrumbs:    
                    return (50, bright, bright) # produces cyan

        return (bright, dark, bright) # produces purple