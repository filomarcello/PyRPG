"""
Created on 20/giu/2015
Modified: 07/08/2016 - Container subclasses Items.

@author: marcello
"""

class Container(object):
    """Base class for items container.-"""

    def __init__(self, itemlist: list = []):
        """Constructs a Container with a list of items."""
        self._items = itemlist
    
    def get_weight(self):
        """Get the total weight of the items contained."""
        return sum([i.get_weight() for i in self._items])
    
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