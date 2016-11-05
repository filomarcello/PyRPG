"""
Created on 06/apr/2015

@author: marcello
"""
from environment.tile import Tile


class Map:
    """Abstract base class for map in RPG game"""
    
    def __init__(self, tiles=[[]], name: str = 'map', info: str = ''):
        """Builds a map with a 2-D list of Tiles."""

        self._tiles = tiles
        self._dim = len(self._tiles), len(self._tiles[0])
        self._name = name
        self._info = info


    def get_tile(self, x, y) -> Tile:
        """Returns the tile in (x, y)."""
        return self._tiles[x][y]

    def set_tile(self, x, y, tile):
        """Sets tile in map (x, y) position."""
        self._tiles[x][y] = tile


    def view(self, x1: int, y1: int, x2: int, y2: int):
        """Returns the tile views from tile (x, y) to (x1, y1).

         (0, 0) is in top-right corner as in screen. x1 <= x2 and y1 <= y2
         """

        l = []
        v = []
        for x in range(x1, x2 + 1):

            for y in range(y1, y2 + 1):
                l.append(self.get_tile(x, y).view)

            v.append(l)
            l = []

        return v

    def view_all(self):
        """Returns all the tiles in the map."""
        return self.view(0, 0, self._dim[0] - 1, self._dim[1] - 1)

