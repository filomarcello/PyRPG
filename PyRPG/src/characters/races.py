'''
Created on 01/mag/2015

@author: marcello
'''

class Race(object):
    '''Implements the 'race' in a RPG game.
    
    As expected Race classes may be Human, Elves, Dwarves, etc.
    '''

    def __init__(self, name: str = 'human', mods: 'Modifier' = None):
        '''Specifies the race name and the modifiers (Modifier class).
        
        >>> b = Race(name='Bugbear')
        >>> print(b)
        Race: Bugbear
        '''
        self._name = name
        self._modifiers = mods
        
    def __str__(self):
        return 'Race: ' + self._name
    
    
# testing by doctest         
if __name__ == "__main__":
    import doctest
    doctest.testmod() 