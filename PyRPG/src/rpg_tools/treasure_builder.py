'''
Created on 06/apr/2015

@author: marcello

Functions for creating money, precious, and treasures.
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

def jeweler() -> 'Gem':
    '''Random gem using AD&D 2nd edition rules. 
    
    TODO TESTS
    '''
    pass