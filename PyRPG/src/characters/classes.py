'''
Created on 01/mag/2015

@author: marcello
'''

class Cls(object):
    '''Cls (for class) is the 'profession' of the character.
    
    May be military, magic users, clerics, vagabond, etc.
    '''

    def __init__(self, name: str = 'warrior', mods: 'Modifier' = None):
        '''Specifies the race name and the modifiers (Modifier class).
        
        >>> w = Cls()
        >>> print(w)
        Class: warrior
        '''
        self._name = name
        self._modifiers = mods
        
    def __str__(self):
        return 'Class: ' + self._name
    
    
# testing by doctest         
if __name__ == "__main__":
    import doctest
    doctest.testmod() 