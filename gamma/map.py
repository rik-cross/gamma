from math import ceil
from .gamma import tileManager

class Map:

    def __init__(self,
    
        # optional parameters
        tiles = None,
        tileSize = 32,
        name = None,
        alpha = 255,
        mapImages = None
    
    ):   

        self.MAX_MAPSIZE = 512
        self.tileSize = tileSize

        # 'tiles' is a 2D array of strings, which are keys to Tile objects
        if tiles is None:
            self.tiles = [ [ 'none' for w in range(self.MAX_MAPSIZE) ] for h in range(self.MAX_MAPSIZE) ]
        else:
            self.tiles = tiles
        
        self.setDimensions()
        
        self.name = name
        self.alpha = alpha

        # map images
        if mapImages is None:
            self.mapImages = []
        else:
            self.mapImages = mapImages
        
        self.editorMode = False

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
    
    # set the tile at specified map (not world) coordinates
    def setTile(self, x, y, tileString):
        self.tiles[y][x] = tileString
        self.setDimensions()

    # returns the tile at specified world coordinates
    def getTileAtPosition(self, x, y):
        xTile = int(x // self.tileSize)
        yTile = int(y // self.tileSize)
        return tileManager.tiles[self.tiles[yTile][xTile]]

    # returns a list of all tiles of a specified type
    # each list item is a set of (x,y) world coordinates
    def getAllTilesOfType(self, type):
        tilePos = []
        for r in range(self.h_map):
            for c in range(self.w_map):
                tile = self.tiles[r][c]
                if tile == type:
                    tilePos.append((c*self.tileSize, r*self.tileSize))       
        return tilePos

    # returns an (x,y) tuple with map center coordinates
    def getMapCenter(self):
        return (self.h_real//2,self.w_real//2)

    # draw map to the specified dimensions
    def drawThumbnail(self, scene, centerX, centerY, maxWidth, maxHeight):

        # calculate largest tile size that will fit
        tileSize = min(
            int(maxWidth / self.w_map),
            int(maxHeight / self.h_map)
        )

        # calculate position based on size
        xPos = int(centerX - ((tileSize*self.w_map)/2))
        yPos = int(centerY - ((tileSize*self.h_map)/2))

        # loop through each tile
        for r in range(self.h_map):
            for c in range(self.w_map):

                # draw tile image (not 'render'), if one exists
                tile = self.tiles[r][c]
                if tileManager.tiles[tile].image is not None:
                    newX = ceil(xPos + c*(tileSize))
                    newY = ceil(yPos + r*(tileSize))
                    tileManager.tiles[tile].draw(scene, newX, newY, tileSize, editorMode=self.editorMode)

    # draw the map, by sending each tile to the renderer
    def draw(self, scene, x=0, y=0, z=1):

        # loop through each tile
        for r in range(self.h_map):
            for c in range(self.w_map):

                # send tile image to the renderer (if one exists)
                tile = self.tiles[r][c]
                if tileManager.tiles[tile].image is not None:
                    newX = x + c*(self.tileSize*z)
                    newY = y + r*(self.tileSize*z)
                    newSize = self.tileSize*z
                    tileManager.tiles[tile].render(scene, newX, newY, newSize, alpha=self.alpha, editorMode=self.editorMode)

