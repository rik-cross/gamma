import math
from .tiles import Tile
from .map_image import MapImage

class Map:

    def __init__(self, tiles=None, tileSize=32):
        self.MAX_MAPSIZE = 512
        self.tileSize = tileSize
        self.mapImages = []
        # 'tiles' is a 2D array of strings, which are keys to Tile.tiles
        if tiles is None:
            self.tiles = [ [ 'none' for w in range(self.MAX_MAPSIZE) ] for h in range(self.MAX_MAPSIZE) ]
        else:
            self.tiles = tiles
        self.setDimensions() 

    def setDimensions(self):

        # calculate height
        lastNonEmptyRow = 0
        for row in range(len(self.tiles)):
            for column in self.tiles[row]:
                if column != 'none':
                    lastNonEmptyRow = row + 1
                    break

        # calculate width
        longestRow = 0
        for row in self.tiles:
            for tileNumber in range(len(row)):
                if row[tileNumber] != 'none':
                    if tileNumber + 1 > longestRow:
                        longestRow = tileNumber + 1

        # set dimensions
        # h_map and w_map store the dimension in tile numbers
        self.h_map = lastNonEmptyRow
        self.w_map = longestRow
        # h_real and w_real store the dimension in pixel numbers
        self.h_real = self.h_map * self.tileSize
        self.w_real = self.w_map * self.tileSize
    
    def setTile(self, x, y, tileString):
        self.tiles[y][x] = tileString

    def getTileAtPosition(self, x, y):
        xTile = int(x // self.tileSize)
        yTile = int(y // self.tileSize)
        return Tile.tiles[self.tiles[yTile][xTile]]

    def getAllTilesOfType(self, type):
        tilePos = []
        for r in range(self.h_map):
            for c in range(self.w_map):
                tile = self.tiles[r][c]
                if tile == type:
                    tilePos.append((c*self.tileSize, r*self.tileSize))       
        return tilePos

    def getMapCenter(self):
        return (self.h_real//2,self.w_real//2)

    def draw(self, screen, x, y, z):
        for r in range(self.h_map):
            for c in range(self.w_map):
                tile = self.tiles[r][c]
                if Tile.tiles[tile].image is not None: 
                    newX = x + c*(self.tileSize*z)
                    newY = y + r*(self.tileSize*z)
                    newWidth = math.ceil(self.tileSize * z)
                    newHeight = math.ceil(self.tileSize * z)
                    Tile.tiles[tile].draw(screen, newX, newY, newWidth, newHeight)