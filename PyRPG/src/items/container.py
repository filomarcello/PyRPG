"""
Created on 20/giu/2015
Modified: 07/08/2016 - Container subclasses Items.

@author: marcello
"""

from items.item import Item

class Container(Item):
    """Base class for items container."""

    def __init__(self, name: str = 'container',
                 weight: float = 0.0,
                 items: list = []):
        """Constructs a Container with a list of items."""

        super().__init__(name=name, weight=weight)
        self._items = items

    @property
    def weight(self):
        """Returns the own weight plus these of the contained items."""
        return sum((w.weight for w in self._items)) + self._weight

    @weight.setter
    def weight(self, weight):
        """Set the Container own weight, items weights remain unaltered."""
        self._weight = weight

    
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
    
    
# testing by doctest         
if __name__ == "__main__":
    import doctest
    doctest.testmod() 