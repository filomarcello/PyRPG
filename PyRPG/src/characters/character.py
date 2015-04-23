'''
Created on 06/apr/2015

@author: marcello
'''

import actions.Actions as Actions

class Character(object):
    '''Base class for a RPG character.
    
    This class implements a simple character having the name as the only 
    property.
    '''
    
    def __init__(self, name: str = 'Character'):
        '''Makes a character with its name'''
        self.name = name
    
    def __str__(self):
        return 'Character: ' + self.name
        
        
class RPGCharacter(Character):
    '''A minimal but complete RPG character.
    
    This class implements a RPG character with her/his name, race, attributes, 
    actions, inventory.
    Added until now:
    - actions
    '''
    
    def __init__(self, name: str, actions: Actions):
        super().__init__(name)
        self.actions = actions   