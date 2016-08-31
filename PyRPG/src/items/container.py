"""
Created on 20/giu/2015
Modified: 07/08/2016 - Container subclasses Items.

@author: marcello
"""
from collections import Iterable

from items.item import Item

class Container(Item):
    """Base class for items container."""

    def __init__(self, name: str = 'container',
                 weight: int = 0,
                 items: list = []):
        """Constructs a Container with a list of items."""

        super().__init__(name, weight)
        self._items = items


    @property
    def weight(self):
        """Returns the own weight plus these of the contained items."""
        if self._items:
            return sum((i._weight for i in self._items)) + self._weight
        else:
            return self._weight


    @weight.setter
    def weight(self, weight):
        """Set the Container own weight, items weights remain unaltered."""
        self._weight = weight


    def __iadd__(self, item):
        """Inplace addition of Item object(s) in the container.

        May be a single Item object or a iterable of Item objects.
        """
        if isinstance(item, Iterable):
            self._items += item
        else:
            self._items.append(item)
        return self

    def __isub__(self, item):
        """Inplace subtraction of a Item object in the container.

        May be a single Item object or a iterable of Item objects.
        """
        if isinstance(item, Iterable):
            for i in item:
                self._items.remove(i)
        else:
            self._items.remove(item)
        return self

    
    
