""" created 18/12/2015
author: marcello
"""

class ItemCollector:
    """Base class for set of items.

    E.g. chests, sacks, backpacks, inventories, etc.
    """

    def __init__(self, items: list = []):
        self._items = items

    # properties
    @property
    def weight(self) -> float:
        return sum([i.weight for i in self._items])

    @property
    def items(self) -> list:
        return self._items

    @items.setter
    def items(self, items: list) -> None:
        self._items = items

    # operators
    def __add__(self, other):
        self._items.append(other)
        return self

    def __iadd__(self, other):
        self._items.append(other)
        return self

    def __sub__(self, other):
        self._items.remove(other)
        return self

    def __isub__(self, other):
        self._items.remove(other)
        return self

    def __contains__(self, item):
        return item in self._items
