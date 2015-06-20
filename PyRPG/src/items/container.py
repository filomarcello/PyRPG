'''
Created on 20/giu/2015

@author: marcello
'''

class Container(object):
    '''Base class for items container.-'''

    def __init__(self, itemlist: list = []):
        '''Constructs a Container with a list of items.'''
        self.items = itemlist
    
    def get_weight(self):
        '''Get the total weight of the items contained.
        
        >>> from items.item import Item
        >>> itemlist = [Item(weight=1.0), Item(weight=10.0), Item(weight=1.5)]
        >>> c = Container(itemlist)
        >>> c.get_weight()
        12.5
        '''
        return sum([i.get_weight() for i in self.items])
    
    
# testing by doctest         
if __name__ == "__main__":
    import doctest
    doctest.testmod() 