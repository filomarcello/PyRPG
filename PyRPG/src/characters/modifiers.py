'''
Created on 23/apr/2015

@author: marcello

Updated 20/06/2015: values can also be string or whatever.
'''

class Modifier(object):
    '''Class that maps modifiers onto the actions.
    
    This class should be considered as a dict with actions names as keys and 
    values as relative numbers to be added to the character action. Values can
    also be string or boolean.
    Each item, ability or whatever has a Modifier class. The character class
    will manage them.
    '''

    def __init__(self, actions: 'Actions'):
        '''Build an empty Modifiers with Actions names.
        
        >>> from characters.actions import Actions
        >>> a = Actions()
        >>> m = Modifier(a)
        >>> print(m)
        Modifier: 1 modifications
        '''
        self._modifiers = {k: 0 for k in actions._actions.keys()}
        
    def add_modifier(self, name: str, value):    
        '''Add the modifier value to the name action.'''
        self._modifiers[name] = value
        
    def get_modifier(self, name: str):
        '''Returns the value of a modifier.'''
        return self._modifiers[name]
    
    def __str__(self):
        return 'Modifier: {n} modifications'.format(n=len(self._modifiers))
    

# testing by doctest         
if __name__ == "__main__":
    import doctest
    doctest.testmod() 
        
    
        