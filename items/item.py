""" Created 16/11/15
author: marcello
"""

from meta.modifier import Modifier

class Item:
    """Base abstract class for a generic item."""

    def __init__(self, name: str = 'item', weight: float = 0.0):
        """Absolutely generic item."""
        self._name = name
        self._weight = weight

    @property
    def weight(self):
        """Weight property of the Item."""
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        self._weight = weight

    @property
    def name(self):
        """Name property of the Item."""
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    def __str__(self):
        return 'Item:{s._name}, Weight:{s._weight}'.format(s=self)


class RPGItem(Item, Modifier):
    """Base class for a generic RPG item.

    RPGItem extends also Modifier class. This allow to bind modifiers to items,
    useful for magic items.
    """

    def __init__(self, name: str, weight: float, mods: dict):
        Item.__init__(self, name, weight)
        Modifier.__init__(self, mods)

