""" created 09/12/2015
author: marcello
"""

class Terrain:
    """Base class for terrain elements."""

    def __init__(self, name: str,
                 g_locked: bool = False,
                 a_locked: bool = False,
                 u_locked: bool = False,
                 image = None):
        """Implements a terrain type.

        name -- [string] terrain name
        g_locked -- [bool] True if the ground is not accessible to characters
        a_locked -- [bool] True if not accessible by flyiers
        u_locked -- [bool] True if not accessible by underground diggers
        image -- the terrain appearance
        """

        self._name = name
        self._image = image
        self.g_locked = g_locked
        self.u_locked = u_locked
        self.a_locked = a_locked


    # properties
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, im):
        self._image = im


# TODO: inheritance with modifier for movement and other
