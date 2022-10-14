class Distances():
    def __init__(self, root):
        self.root = root
        self.cells = dict()
        self.cells[self.root] = 0

    def get(self, cell):
        return self.cells[cell]

    def set(self, cell, distance):
        self.cells[cell] = distance

    def getCells(self):
        return self.cells.keys()

    def pathTo(self, goal):
        current = goal 

        breadcrumbs = Distances(self.root)
        breadcrumbs.set(current, self.cells[current])

        while current != self.root:
            for neighbor in current.links:
                if self.cells[neighbor] < self.cells[current]:
                    breadcrumbs.set(neighbor, self.cells[neighbor])
                    current = neighbor 
                    break 

        return breadcrumbs 

    def max(self):
        maxDistance = 0
        maxCell = self.root 

        for cell, distance in self.cells.items():
            if distance > maxDistance:
                maxCell = cell 
                maxDistance = distance 

        return [maxCell, maxDistance]