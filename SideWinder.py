import numpy as np
from random import choice

class SideWinder():
    def on(grid):
        for row in grid.eachRow():
            run = np.array([])

            for cell in row:
                run = np.append(run, [cell])

                atEasternBoundary = (cell.east == None)
                atNorthernBoundary = (cell.north == None)

                shouldCloseOut = atEasternBoundary or (atNorthernBoundary == False and choice(range(2)) == 0)

                if shouldCloseOut:
                    member = choice(run)
                    if member.north: member.link(member.north)
                    run = np.array([])
                else:
                    cell.link(cell.east)

        return grid