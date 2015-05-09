'''
Created on 06/apr/2015

@author: marcello

Class and functions for creating money, precious, and treasures.
'''

from items.treasure import Gem
from rpg_tools.dices import DiceTable

# constants

# gems: following AD&D 2nd edition rules               
# d100                 weight value   type
ADD2_GEMS_VALUE_TABLE = [(25, (10,   'ornamental'  )),
                         (25, (50,   'semiprecious')),
                         (20, (100,  'fancy'       )),
                         (20, (500,  'precious'    )),
                         (9,  (1000, 'gems'        )),
                         (1,  (5000, 'jewel'       )),]

ADD2_GEMS_PROB_MOD = 0.10 # prob to have a modified gem
ADD2_GEMS_VARIATION_TABLE = '' # TODO
ADD2_GEMS_EXT_DESCRIPTIONS = '' # TODO

class Jeweler(DiceTable):
    '''Random gem creator.'''
    
    def __init__(self, tab: tuple):
        '''tab as in DiceTable class constructor.'''
        super().__init__(tab)
        
    def craft(self) -> 'Gem':
        '''Return a single gem.
        
        >>> j = Jeweler(ADD2_GEMS_VALUE_TABLE)
        >>> isinstance(j.craft(), Gem)
        True
        '''
        value, descr = self.throw()
        # here implement extended description
        return Gem(value, descr)
    
    def multiple_craft(self, n: int) -> list:
        '''Return a list of n gems.
        
        >>> j = Jeweler(ADD2_GEMS_VALUE_TABLE)
        >>> gg = j.multiple_craft(5)
        >>> len(gg)
        5
        >>> all(map(lambda x: isinstance(x, Gem), gg))
        True
        '''
        return [self.craft() for i in range(n)]
    
    def _ext_descr(self):
        '''Add ad extended description to the creating gem.
        TODO
        '''
        pass
    
    
# test
if __name__ == '__main__':
    import doctest
    doctest.testmod()
        