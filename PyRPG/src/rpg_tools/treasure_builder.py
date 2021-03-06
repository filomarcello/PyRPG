'''
Created on 06/apr/2015

@author: marcello

Class and functions for creating money, precious, and treasures.
'''

from items.treasure import Gem, Money, DD_CURRENCIES
from rpg_tools.dices import DiceTable, Dice
import random as rand


# constants for hoard builder

# gems: following AD&D 2nd edition rules 
#                   value  descriprion  
ADD2_GEMS_LEVELS = ((10,   'ornamental'  ),
                    (50,   'semiprecious'),
                    (100,  'fancy'       ),
                    (500,  'precious'    ),
                    (1000, 'gems'        ),
                    (5000, 'jewel'       ))

ADD2_GEMS_BASIC_DESCR = tuple(d[1] for d in ADD2_GEMS_LEVELS)
                              
# prob is for 1d100, level is from ADD2_GEMS_LEVELS
ADD2_GEMS_VALUE_TABLE = tuple((prob, level) for prob, level in 
                             zip((25, 25, 20, 20, 9, 1), ADD2_GEMS_LEVELS))

ADD2_GEMS_PROB_MOD = 0.10 # prob to have a modified gem

# AD&D 2nd edition Gem modifyier function
def _ADD2_gem_modificator(gem: 'Gem') -> 'Gem':
    n = rand.randint(1, 6)
    if   n == 2:
        gem._value *= 2
    elif n == 3:
        gem._value *= 1.0 + (rand.randint(1, 6) * 10) / 100
        gem._value = int(gem._value)
    elif n == 4:
        gem._value *= 1.0 - (rand.randint(1, 4) * 10) / 100
        gem._value = int(gem._value)
    elif n == 5:
        gem._value /= 2
    elif n == 1: # promote gem 
        one = 1
        while one == 1 and gem._value < 100000:
            l = ADD2_GEMS_BASIC_DESCR.index(gem._description)
            if l < 6:
                gem._value, gem._description = ADD2_GEMS_BASIC_DESCR[l + 1]
            else:
                gem._value *= 2
            one = rand.randint(1, 6)
    elif n == 6: # demote gem
        six = 6
        counter = 0
        while six == 6 and gem._value > 1 and counter < 6:
            l = ADD2_GEMS_BASIC_DESCR.index(gem._description)
            if l > 1:
                gem._value, gem._description = ADD2_GEMS_BASIC_DESCR[l - 1]
            else:
                gem._value /= 2
                gem._value = int(gem._value)
            one = rand.randint(1, 6)
            counter += 1
        
    return gem

# TODO arrange descriptions
ADD2_GEMS_EXT_DESCRIPTIONS = {'ornamental': 
        ('Azurite: Opaque, mottled deep blue',
        'Banded Agate: Brown, blue, red, and white stripes',
        'Blue Quartz: Transparent pale blue',
        'Eye Agate: Gray, white, brown, blue, and green circles',
        'Hematite: Gray-black',
        'Lapis Lazuli: Light or dark blue with yellow flecks',
        'Malachite: Striated light and dark green',
        'Moss Agate: Pink, yellow-white with gray-green moss-like markings',
        'Obsidian: Jet black',
        'Rhodochrosite: Light pink',
        'Tiger Eye Agate: Rich golden brown with dark striping',
        'Turquoise: Aqua with darker mottling'),
                              'semiprecious':
        ('Bloodstone: Dark gray with red flecks',
        'Carnelian: Orange to red-brown',
        'Chalcedony: White',
        'Chrysoprase: Translucent apple to emerald green',
        'Citrine: Pale yellow brown',
        'Jasper: Blue, black to brown',
        'Moonstone: White with pale blue hue',
        'Onyx: Black, white, or bands of both',
        'Rock Crystal: Clear, transparent',
        'Sardonyx: Bands of red and white',
        'Smoky Quartz: light gray, yellow, brown or blue',
        'Star Rose Quartz: Smoky rose with white star center',
        'Zircon: Clear pale aqua',),
                               'fancy':
        ('Amber: Transparent golden',
        'Alexandrite: Dark green',
        'Amethyst: Purple crystal',
        'Chrysoberyl: green or yellow green',
        'Coral: Pink to crimson',
        'Garnet: Deep red to violet crystal',
        'Jade: Light to dark green or white',
        'Jet: Deep black',
        'Pearl: Pure white, rose, to black',
        'Spinel: Red, red-brown, green, or deep blue',
        'Tourmaline: Pale green, blue, brown, or red',),
                                'precious':
        ('Aquamarine: pale blue green',
         'Garnet: Deep red to violet crystal',
         'Pearl: Pure white, rose, to black',
         'Peridot: Olive green',
         'Spinel: Red, red-brown, green, or deep blue',
         'Topaz: Golden yellow',),
                                 'gems':
        ('Black Opal: Dark green with black mottling and golden flecks',
        'Fire Opal: Fiery red',
        'Opal: Pale blue with green and gold mottling',
        'Oriental Amethyst: Deep purple',
        'Oriental Topaz: Fiery yellow',
        'Sapphire: Clear to medium blue',),
                                  'jewels':
        ('Black Sapphire: Rich black with highlights',
        'Diamond: Clear blue-white, rich blue, yellow, or pink',
        'Emerald: Brilliant green',
        'Jacinth: Fiery orange',
        'Oriental Emerald: Bright green',
        'Ruby: Clear to deep crimson red',
        'Star Ruby: Translucent ruby with white star highlights',
        'Star Sapphire: Translucent blue with white star highlights',),}


class Jeweler(DiceTable):
    '''Random gem creator.'''
    
    def __init__(self, tab: tuple):
        '''tab as in DiceTable class constructor.'''
        super().__init__(tab)
        
    def craft(self) -> 'Gem': # TODO testing
        '''Return a single gem.
        
        >>> j = Jeweler(ADD2_GEMS_VALUE_TABLE)
        >>> isinstance(j.craft(), Gem)
        True
        '''
        value, descr = self.throw()
        g = Gem(value, descr)
        
        if self.throw_this('1d100') < 11: # modification
            _ADD2_gem_modificator(g)
                    
        g = self._ext_descr(g) # add extended description
        
        return g
    
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
    
    def _ext_descr(self, gem):
        '''Add ad extended description to the creating gem.
        TODO
        '''
        gem._description = gem._description + ' ' + \
                rand.choice(ADD2_GEMS_EXT_DESCRIPTIONS[gem._description])
                
        return gem
    
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
        