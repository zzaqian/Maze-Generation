import numpy as np

class HuntAndKill():
    def on(grid):
        current = grid.randomCell()

        while current:
            unvisitedNeighbors = np.array([])
            for neighbor in current.neighbors():
                if len(neighbor.links) == 0: unvisitedNeighbors = np.append(unvisitedNeighbors, [neighbor])

            if unvisitedNeighbors.size > 0:
                neighbor = np.random.choice(unvisitedNeighbors) # np.random.choice returns the object when there is only one output
                current.link(neighbor)
                current = neighbor 
            else: # switch to hunt phase
                current = None 

                for cell in grid.eachCell():
                    if len(cell.links) == 0:
                        visitedNeighbors = np.array([])
                        for neighbor in cell.neighbors():
                            if len(neighbor.links) > 0: visitedNeighbors = np.append(visitedNeighbors, [neighbor])

                        if visitedNeighbors.size > 0:
                            current = cell 

                            neighbor = np.random.choice(visitedNeighbors)
                            current.link(neighbor) 

                            break 

        return grid

    def onChosen(grid):
        unvisitedCells = np.array([])
        for cell in grid.eachCell():
            unvisitedCells = np.append(unvisitedCells, [cell])
        np.random.shuffle(unvisitedCells) # shuffle the array to randomize

        current = grid.randomCell()
        firstIndex = np.where(unvisitedCells == current)[0] # the output of the where function is a tuple of arrays
        unvisitedCells = np.delete(unvisitedCells, firstIndex)

        while current:
            unvisitedNeighbors = np.array([])
            for neighbor in current.neighbors():
                if len(neighbor.links) == 0: unvisitedNeighbors = np.append(unvisitedNeighbors, [neighbor])

            if unvisitedNeighbors.size > 0:
                neighbor = np.random.choice(unvisitedNeighbors) # np.random.choice returns the object itself when there is only one output
                current.link(neighbor) 
                current = neighbor 
                index = np.where(unvisitedCells == current)[0] 
                unvisitedCells = np.delete(unvisitedCells, index)
            else: # switch to hunt phase
                current = None 

                if unvisitedCells.size > 0:
                    for cell in unvisitedCells:
                        visitedNeighbors = np.array([])
                        for neighbor in cell.neighbors():
                            if len(neighbor.links) > 0: visitedNeighbors = np.append(visitedNeighbors, [neighbor])

                        if visitedNeighbors.size > 0:
                            current = cell # delete this cell from unvisitedCells
                            index = np.where(unvisitedCells == current)[0] 
                            unvisitedCells = np.delete(unvisitedCells, index)

                            neighbor = np.random.choice(visitedNeighbors)
                            current.link(neighbor) 
                            
                            break 
                else:
                    pass

        return grid