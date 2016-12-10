"""
Created on 05/apr/2015
Modified: 16/11/2015
          02/08/2016 revised tests
          08/08/2016 weight is now integer
          17/10/2016 revised RPGItem
          07/12/2016 add weight() function to weight an iterable of Item objs

@author: marcello
"""
import collections.abc

##### functions

def weight(items) -> int:
    """Weights a single Item or a Iterable of Item objects."""
    if isinstance(items, collections.abc.Sequence):
        return sum(weight(i) for i in items)
    return items.weight


##### classes

class Item:
    """Base abstract class for a generic item.

    All items have at least a name and a weight.
    """
    
    def __init__(self, name: str = 'item', weight: int = 0):
        """Absolutely generic item."""
        self._name = name
        self._weight = weight

    @property
    def weight(self):
        """Weight property of the Item."""
        return self._weight

    @weight.setter
    def weight(self, w: int):
        self._weight = w

    @property
    def name(self):
        """Name property of the Item."""
        return self._name

    @name.setter
    def name(self, n: str):
        self._name = n
        
    def __str__(self):
        return 'Item:{s._name}, Weight:{s._weight}'.format(s=self)
