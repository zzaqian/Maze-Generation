from random import choice, random

class BinaryTree():
    def on(grid):
        for cell in grid.eachCell():
            neighbors = list()
            if cell.north: neighbors.append(cell.north)
            if cell.east: neighbors.append(cell.east)


            if len(neighbors) > 0: 
                neighbor = choice(neighbors) if len(neighbors) < 2 or random() > -1 else neighbors[0]
                if neighbor: cell.link(neighbor)

        return grid