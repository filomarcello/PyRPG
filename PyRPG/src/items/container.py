"""
Created on 20/giu/2015
Modified: 07/08/2016 - Container subclasses Items.

@author: marcello
"""

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
        """Inplace addition of a Item object in the container."""
        self._items.append(item)
        return self

    def __isub__(self, item):
        """Inplace subtraction of a Item object in the container."""
        self._items.remove(item)
        return self


    
class Inventory(Container):
    '''Implements the character inventory, i.e. backpack, bags, etc.
    
    The items are not equipped, so they influence the character only by their
    weight.
    '''
    def __init__(self, itemlist: list = []):
        '''items is a list of Items objects or subclasses.'''
        super().__init__(itemlist)


class Suit(Container):
    '''The collection of the items worn or in using by the character'''
    pass


class Armament(Suit):
    '''The collection of weapons and armors equipped by the character'''
    pass
    
    
