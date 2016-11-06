"""
Created on 20/apr/2015

@author: marcello
"""

class Tile(object):
    """Abstract class for tiles in map.

    Each tile has the following layers (bottom to top):
    - terrain: grass, water, mountains, etc.
    - terrain objects: stones, trees, buildings, etc,
    - adventure objects: chests, dropped items, etc.

    Properties:
    - passable: false if blocked to walk
    - explored: true if terrain is known
    - fog: false if fog of war disabled

    View: text or image of the tile showed in the map.
    """
    
    def __init__(self, terrain=None,
                 ter_objs: list = [], adv_objs: list = [],
                 view=None):
        """Builds a tile with the following arguments:

        terrain -- the type of terrain in tile
        ter_objs -- list of terrain objects
        adv_objs -- list of adventure objects
        view -- the appearance of tile in the map.
        """

        self._terrain = terrain
        self._ter_objs = ter_objs
        self._adv_objs = adv_objs
        self._view = view

        # properties

    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, v):
        self._view = v





