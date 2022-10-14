from random import choice

class AldousBroder():
    def on(grid):
        cell = grid.randomCell()
        unvisited = grid.size() - 1

        while unvisited > 0:
            neighbor = choice(cell.neighbors())

            if len(neighbor.links) == 0:
                cell.link(neighbor)
                unvisited -= 1

            cell = neighbor 

        return grid