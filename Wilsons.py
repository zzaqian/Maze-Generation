import numpy as np
from random import choice

class Wilsons():
    def on(grid):
        unvisited = np.array([])
        for cell in grid.eachCell():
            unvisited = np.append(unvisited, [cell])

        first = choice(range(unvisited.size))
        unvisited = np.delete(unvisited, first)

        while unvisited.size > 0:
            cell = choice(unvisited)
            path = np.array([cell])

            while cell in unvisited:
                cell = choice(cell.neighbors())
                position = np.where(path == cell)[0] # the output of the where function is a tuple of arrays

                if position.size > 0:
                    path = path[:position[0]+1]
                else:
                    path = np.append(path, [cell])

            for i in range(path.size - 1):
                path[i].link(path[i+1])
                index = np.where(unvisited == path[i])[0]
                unvisited = np.delete(unvisited, index)

        return grid