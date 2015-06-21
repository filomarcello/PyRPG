'''
Created on 05/apr/2015

@author: marcello

Update 21/06/2015: Wearable now extends RPGItem
'''
from items.item import RPGItem

class Wearable(RPGItem):
    '''Base abstract class for a generic wearable item.
    
    May include armors, helmet, robe, gloves, boots, etc.
    '''
    
    def __init__(self, name: str, 
                 weight: float = 0.0, 
                 worn: bool = False,
                 magic: bool = False):
        '''Build a Wearable with name, weight and boolean worn.
        
        >>> w = Wearable(name='boots')
        >>> print(w)
        Wearable: boots
        Weight: 0.0
        Worn: False
        >>> w.get_weight()
        0.0
        '''
        super().__init__(name, weight, magic)
        self._worn = worn
        
    def is_worn(self):
        '''Return True if the Wearable is worn
        
        >>> w = Wearable(name='gloves', weight=0.5, worn=True)
        >>> w.is_worn()
        True
        '''
        return self._worn
    
    def __str__(self):
        return 'Wearable: {s._name}\nWeight: {s._weight}\nWorn: {s._worn}'\
            .format(s=self)
    
    
# testing by doctest         
if __name__ == "__main__":
    import doctest
    doctest.testmod() 