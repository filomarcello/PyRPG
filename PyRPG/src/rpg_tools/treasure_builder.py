'''
Created on 06/apr/2015

@author: marcello

Class and functions for creating money, precious, and treasures.
'''

from items.treasure import Gem, Money, DD_CURRENCIES
from rpg_tools.dices import DiceTable, Dice


# constants for hoard builder

# gems: following AD&D 2nd edition rules               
# d100                 weight value   type
ADD2_GEMS_VALUE_TABLE = ((25, (10,   'ornamental'  )),
                         (25, (50,   'semiprecious')),
                         (20, (100,  'fancy'       )),
                         (20, (500,  'precious'    )),
                         (9,  (1000, 'gems'        )),
                         (1,  (5000, 'jewel'       )),)

ADD2_GEMS_PROB_MOD = 0.10 # prob to have a modified gem
ADD2_GEMS_VARIATION_TABLE = '' # TODO
ADD2_GEMS_EXT_DESCRIPTIONS = '' # TODO

# money: following AD&D 2nd edition rules



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
    
class Mint(Dice):
    '''Class for random building money.
    
    It is a subclass of Dice. Initialized to '1d100', used to check if such
    coin in present in the treasure.
    '''
    
    def __init__(self):
        super().__init__('1d100')
    
    def coinage(self, tab: dict, elecplat: str) -> 'Money':
        '''Return a random Money object based to tab probabilities.
        
        tab has to be as following:
        {coin_type: (prob_coin, dice_string, multiplier), ...}
        coin_type: copper, silver, gold, electrum, platinum
        prob_coin: probability (0-100) that coin type is present in the hoard
        dice_string: string to build the dice to random create
        multiplier: the number to multiply the result of dice_string
        
        elecplat: 'electrum' or 'platinum'. Whatever else to choose randomly
        
        >>> m = Mint()
        >>> g = m.coinage({'copper': (100, '1d10', 1000), 'silver': (100, '1d6', 1000), 'gold':   (25,  '1d6', 100), 'electrum': (25, '1d4', 10), 'platinum': (25, '1d4', 10)}, elecplat='platinum')
        >>> type(g)
        <class 'items.treasure.Money'>
        '''
        m = {}
        for c in DD_CURRENCIES:
            if self.throw() < tab[c][0]: # if 1d100 < prob_coin
                m[c] = self.throw_this(tab[c][1]) * tab[c][2]
            else:
                m[c] = 0
        
        if elecplat == 'electrum':
            m['platinum'] = 0
        elif elecplat == 'platinum':
            m['electrum'] = 0
        else:
            if self.throw_this('1d2') == 1:
                m['platinum'] = 0
            else:
                m['electrum'] = 0
            
        return Money(m)
    
# test
if __name__ == '__main__':
    import doctest
    doctest.testmod()
        