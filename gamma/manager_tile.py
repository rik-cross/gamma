import pygame

class TileManager:
    
    def __init__(self):
        self.tiles = {}

    def addTile(self, tile):
        self.tiles[tile.name] = tile

    def getTile(self, key):
        if key not in self.tiles.keys():
            return None
        return self.tiles[key]
