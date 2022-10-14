from random import choice, shuffle

class RecursiveBacktracker():
    def on(grid, startAt=None): # the parameter startAt should be a cell
        if startAt == None:
            start = grid.randomCell() # default to random cell in the grid
        else:
            start = startAt
        
        stack = list()
        stack.append(start) 

        while len(stack) > 0:
            current = stack[-1]
            neighbors = list()
            for neighbor in current.neighbors():
                if len(neighbor.links) == 0: neighbors.append(neighbor) # find unvisited neighbors

            if len(neighbors) == 0:
                stack.pop(-1) 
            else:
                neighbor = choice(neighbors) 
                current.link(neighbor) 
                stack.append(neighbor) 

        return grid 

    def onRecursion(grid, current): # implicit recursion as opposed to explicit recursion (using a stack)
        neighbors = current.neighbors()
        shuffle(neighbors)
        
        for neighbor in neighbors:
            if len(neighbor.links) == 0:
                current.link(neighbor) 
                RecursiveBacktracker.onRecursion(grid, neighbor)

        return grid

