import numpy as np
import pygame

class Mask():
    def fromTXT(file):
        f = open(file) 
        lines = list(map(str.strip, f))
        while len(lines[-1]) < 1:
            lines.pop(-1)

        rows = len(lines) 
        cols = len(lines[0]) 
        mask = Mask(rows, cols) 

        for row in range(mask.rows):
            for col in range(mask.cols):
                if lines[row][col] == "X":
                    mask.set(row, col, False) 
                else:
                    mask.set(row, col, True) 

        return mask

    def fromPNG(file):
        image = pygame.image.load(file) 
        mask = Mask(image.get_height(), image.get_width()) 

        for row in range(mask.rows):
            for col in range(mask.cols):
                if tuple(image.get_at((col, row)))[:3] == (0,0,0): # the color of the pixel is black 
                    mask.set(row, col, False) 
                else: 
                    mask.set(row, col, True) 
                    
        return mask 

    def disk(radius):
        imgWidth = radius * 2
        imgHeight = radius * 2 

        BLACK = (0,0,0) 
        WHITE = (255, 255, 255)

        Surf = pygame.Surface((imgWidth, imgHeight)) 
        Surf.fill(BLACK)

        center = (radius, radius) 
        
        pygame.draw.circle(Surf, WHITE, center, radius) 

        filename = "disk.png" 
        pygame.image.save(Surf, filename) 

        return Mask.fromPNG(filename) 

    def polygon(listofPoints):
        imgWidth = 0
        imgHeight = 0
        
        for i in listofPoints:
            imgWidth = max(imgWidth, i[0]) 
            imgHeight = max(imgHeight, i[1])

        imgWidth +=1
        imgHeight +=1

        BLACK = (0,0,0) 
        WHITE = (255, 255, 255)

        Surf = pygame.Surface((imgWidth, imgHeight)) 
        Surf.fill(BLACK) 
        
        pygame.draw.polygon(Surf, WHITE, listofPoints) 

        filename = "polygon.png" 
        pygame.image.save(Surf, filename) 

        return Mask.fromPNG(filename) 

    def __init__(self, rows, cols):
        self.rows = rows 
        self.cols = cols 
        self.bits = np.full((self.rows, self.cols), True) 

    def get(self, row, col):
        if 0 <= row <= self.rows-1 and 0 <= col <= self.cols-1:
            return self.bits[row, col] 
        else:
            return False 

    def set(self, row, col, isOn):
        self.bits[row, col] = isOn 

    def count(self):
        count = 0 

        for row in range(self.rows):
            for col in range(self.cols):
                if self.bits[row, col]: count += 1 

        return count 

    def randomLocation(self):
        while True:
            row = np.random.choice(np.arange(self.rows))
            col = np.random.choice(np.arange(self.cols)) 

            if self.bits[row, col]: 
                return row, col