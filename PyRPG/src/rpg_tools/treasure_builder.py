'''
Created on 06/apr/2015

@author: marcello

Functions for creating money, precious, and treasures.
'''

from items.treasure import Gem

# constants
# gems                 
# d100                   interval  value    type
ADD2_GEMS_VALUE_TABLE = [((1,  25), (10,   'ornamental'  )),
                         ((26, 50), (50,   'semiprecious')),
                         ((51, 70), (100,  'fancy'       )),
                         ((71, 90), (500,  'precious'    )),
                         ((91, 99), (1000, 'gems'        )),
                         ((0,   0), (5000, 'jewel'       )),]

ADD2_GEMS_PROB_MOD = 0.10

ADD2_GEMS_VARIATION_TABLE = '' # TODO

def jeweler() -> 'Gem':
    '''Random gem using AD&D 2nd edition rules. '''
    pass