'''
Created on 05/apr/2015

@author: marcello
'''

class Item(object):
    '''Base abstract class for a generic item.'''
    
    def __init__(self, name: str = 'noname', weight: float = 0.0):
        '''Absolutely generic item.
        
        >>> i = Item()
        >>> print(i)
        Item: noname
        Weight: 0.0
        '''
        self._name = name
        self._weight = weight
        
    def get_weight(self):
        '''Returns the weight of the Item.
        
        >>> i = Item(weight=12.5)
        >>> i.get_weight()
        12.5
        '''
        return self._weight
        
    def __str__(self):
        return 'Item: {s._name}\nWeight: {s._weight}'.format(s=self)
    
# testing by doctest         
if __name__ == "__main__":
    import doctest
    doctest.testmod() 