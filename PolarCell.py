from Cell import * 

class PolarCell(Cell): 
    def __init__(self, row, col):
        self.row = row
        self.col = col # position
        self.links = dict()
        self.cw = None 
        self.ccw = None 
        self.inward = None
        self.outward = np.array([]) 

    def neighbors(self):
        l = np.array([]) 
        if self.cw: l = np.append(l, [self.cw])
        if self.ccw: l = np.append(l, [self.ccw]) 
        if self.inward: l = np.append(l, [self.inward])
        if len(self.outward) != 0:  l = np.append(l, self.outward) 

        return l 

