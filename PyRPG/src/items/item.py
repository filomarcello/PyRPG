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
    
    
class RPGItem(Item):
    '''Extends the generic Item with modifier.'''
    
    def __init__(self, name: str = 'noname', 
                 weight: float = 0.0,
                 modifier: 'Modifier' = None,
                 magic: bool = False):
        '''modifier is a Modifier class containing modificators.
        
        This class allow item modificators which will be managed by the
        Character class.
        
        >>> from characters.modifiers import Modifier
        >>> from characters.actions import Actions        
        >>> i = RPGItem('thing', 1.0, Modifier(Actions()))
        >>> print(i)
        RPGItem: thing
        Weight: 1.0
        '''
        super().__init__(name, weight)
        self._modifier = modifier
        self._magic = magic
        
    def get_modifier(self):
        '''Returns the modifiers associated with this item.'''
        return self._modifier
    
    def is_magic(self) -> bool:
        return self._magic
    
    def __str__(self):
        return 'RPGItem: {s._name}\nWeight: {s._weight}'.format(s=self)
    
# testing by doctest         
if __name__ == "__main__":
    import doctest
    doctest.testmod() 