"""
Created on 20/giu/2015
Modified: 07/08/2016 - Container subclasses Items.

@author: marcello
"""

import collections
from items.item import Item, weight


class Container(Item):
    """Base class for items container.

    Implements a wrapper for a list of Items.
    Overloads '+=' inplace operator, returning the same Container with a new
    list of Items added and '-=' inplace operator, returning the same Container
    without a list of Items. Doesn't check if Items to be subtracted are in the
    Container.
    """

    def __init__(self, name: str = 'container',
                 weight: int = 0,
                 items: list = []):
        """Constructs a Container with a list of items.

        name   -- name of the container
        weight -- weight of the container
        items  -- list of items to 'put' in the container.
        """
        super().__init__(name, weight)
        self._items = items


    @property
    def weight(self):
        """Returns the own weight plus these of the contained items."""
        if self._items:
            return sum(weight(i) for i in self._items) + self._weight
        else:
            return self._weight


    @weight.setter
    def weight(self, weight):
        """Set the Container own weight, items weights remain unaltered."""
        self._weight = weight

    @property
    def items(self):
        return self._items


    def __iadd__(self, item):
        """Inplace addition of Item object(s) in the container.

        May be a single Item object or a iterable of Item objects.
        """
        if isinstance(item, collections.abc.Sequence):
            self._items += item
        else:
            self._items.append(item)
        return self

    def __isub__(self, item):
        """Inplace subtraction of a Item object in the container.

        May be a single Item object or a iterable of Item objects.
        """
        if isinstance(item, collections.abc.Sequence):
            for i in item:
                self._items.remove(i)
        else:
            self._items.remove(item)
        return self


class Backpack(Container):
    """A backpack has a maximum capacity in items and/or weight."""

    def __init__(self, weight: int, max_items: int, max_weight: int,
                 name: str = 'container'):
        if max_items or max_weight:
            super().__init__(name, weight, items=[])
            self._max_items = max_items or float('inf')
            self._max_weight = max_weight or float('inf')
        else:
            pass # TODO: raise an exception to be impemented

    def __iadd__(self, item): # TODO: partial addition and deletion of other

        if weight(self.items) + weight(item) > self._max_weight:
            return self  # TODO: raise an exception

        if isinstance(item, collections.abc.Sequence):

            if (len(self._items) + len(item) > self._max_items):
                return self # TODO: raise an exception
        else:
            if (len(self._items) == self._max_items) or ():
                return self

        return super().__iadd__(item)

    def __isub__(self, item):
        return super().__isub__(item)









