""" created 09/12/2015
author: marcello
"""

from environment.objects import TerrainObject
from environment.terrains import Terrain


class Tile:
    """Base class for tiles in map."""

    def __init__(self, terrain: Terrain, object: TerrainObject = None):
        self._terrain = terrain
        self._object = object