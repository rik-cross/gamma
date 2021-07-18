import pygame
import math
from .tiles import *
from .map_image import *
import pickle

MAPSIZE = 256

def loadMap(filename, mapImages=[]):
    filename = 'levels/' + filename + '.lvl'
    map =  pickle.load( open( filename, "rb" ) )
    for img in mapImages:
        map.mapImages.append(img)
    return map

def saveMap(map, filename):
    filename = 'levels/' + filename + '.lvl'
    pickle.dump( map, open( filename, "wb" ) )

class Map:

    def __init__(self, map=None, tileSize=32):
        self.tileSize = tileSize
        self.mapImages = []
        if map is None:
            self.map = [ [ 'none' for w in range(MAPSIZE) ] for h in range(MAPSIZE) ]
        elif isinstance(map, str):
            self.loadFromFile(map)
        else:
            self.map = map
        self.setDimensions() 

    def setDimensions(self):

        # calculate height
        lastNonEmptyRow = 0
        for row in range(len(self.map)):
            for column in self.map[row]:
                if column != 'none':
                    lastNonEmptyRow = row + 1
                    break

        # calculate width
        longestRow = 0
        for row in self.map:
            for tileNumber in range(len(row)):
                if row[tileNumber] != 'none':
                    if tileNumber + 1 > longestRow:
                        longestRow = tileNumber + 1

        # set dimensions
        self.h_map = lastNonEmptyRow
        self.w_map = longestRow
        self.h_real = self.h_map * self.tileSize
        self.w_real = self.w_map * self.tileSize
    
    def setTile(self, x, y, tileString):
        self.map[y][x] = tileString

    def getTileAtPosition(self, x, y):
        xTile = int(x // self.tileSize)
        yTile = int(y // self.tileSize)
        return Tile.tiles[self.map[yTile][xTile]]

    def getAllTilesOfType(self, type):
        tilePos = []

        for r in range(self.h_map):
            for c in range(self.w_map):
                tile = self.map[r][c]
                if tile == type:
                    tilePos.append((c*self.tileSize, r*self.tileSize))       

        return tilePos

    def getMapCenter(self):
        return (self.h_real//2,self.w_real//2)

    def draw(self, screen, x, y, z):
        for r in range(self.h_map):
            for c in range(self.w_map):
                tile = self.map[r][c]
                if Tile.tiles[tile].image is not None: 
                    newX = x + c*(self.tileSize*z)
                    newY = y + r*(self.tileSize*z)
                    newWidth = math.ceil(self.tileSize * z)
                    newHeight = math.ceil(self.tileSize * z)
                    Tile.tiles[tile].draw(screen, newX, newY, newWidth, newHeight)