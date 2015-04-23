'''
Created on 20/apr/2015

@author: marcello
'''
from _ast import Str


class Abilities(object):
    '''Base class for ability scores.
    
    Wraps a dictionary being keys the name of the abilities and values
    the scores. The scores must be numbers, whatever type.
    '''

    def __init__(self, abilities: dict = {'strength': 1}):
        self.abilities = abilities
        
    def set_ability(self, ability_name: str, value):
        '''Set the ability_name to the value (numeric).
        
        If 'ability_name' ability does not exist, the function creates a
        new one.
        '''
        self.abilities[ability_name] = value
        
    def get_ability(self, ability_name: str):
        '''Get the value (numeric) of 'ability_name' ability.'''
        return self.abilities[ability_name]
    
    