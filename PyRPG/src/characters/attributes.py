'''
Created on 20/apr/2015

@author: marcello
'''

DD_ABILITIES_NAMES = ['strength', 'dexterity', 'constitution', 'intelligence',
                      'wisdom', 'charisma']

class Abilities(object):
    '''Base class for ability scores.
    
    Wraps a dictionary being keys the name of the abilities and values
    the scores. The scores must be numbers, whatever type.
    '''

    def __init__(self, abilities: dict = {'attack': 1}):
        '''Creates an object with a dict of abilities.
        
        If abilities is not specified uses a standard one:
        >>> ab = Abilities()
        >>> ab.get_ability('attack')
        1
        
        No other abilities has been created:
        >>> ab.get_ability('dementia')
        Traceback (most recent call last):
            ...
        KeyError: 'dementia'
        '''
        self._abilities = abilities
        
    def set_ability(self, ability_name: str, value):
        '''Set the ability_name to the value (numeric).
        
        >>> ab.set_ability('attack', 10)
        >>> ab.get_ability('attack')
        10
        '''
        self._abilities[ability_name] = value
        
    def get_ability(self, ability_name: str) -> 'Number':
        '''Get the value (numeric) of 'ability_name' ability.'''
        return self._abilities[ability_name]
    

class DD_Abilities(Abilities): #TODO: sistemare 
    '''Set then abilities to the standard D&D.
    
    Preset abilities are strength, dexterity, constitution, intelligence,
    wisdom, and charisma. 
    '''
    
    def __init__(self, values: list = [0, 0, 0, 0, 0, 0]):
        '''Order of the values list: str, dex, con, int, wis, cha.
        
        Default are zero values.
        >>> dd_ab = DD_Abilities()
        >>> dd_ab.get_ability('constitution')
        0
        
        This constructor does not check if values are in range for D&D rules:    
        >>> dd_ab2 = DD_Abilities([1000, 3000, -69, 10.25, 858, 0)
        >>> dd_ab2.get_ability('constitution')
        -69
        >>> dd_ab2.get_ability('wisdom')
        '''
        super().__init__(abilities={n: v for n, v 
                                    in zip(DD_ABILITIES_NAMES, values)})
                                    
                                   


# testing by doctest         
if __name__ == "__main__":
    import doctest
    doctest.testmod() 