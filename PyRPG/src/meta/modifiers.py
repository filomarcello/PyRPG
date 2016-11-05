"""
Created on 23/apr/2015

@author: marcello

Updated 20/06/2015: values can also be string or whatever.
        17/10/2016: moved in meta module, revised docstrings and key names.
"""

class Modifier():
    """Class that maps modifiers onto any other features.

    This class should be considered as a dict with names as keys and
    values as relative numbers to be added to the feature. Values can  also be
    string or boolean.
    Characters, items, abilities or whatever may have a Modifier class. The
    management of modifiers is up to the class that wraps them.
    """

    def __init__(self, features):
        """Features can be a string or list of strings. Values set to None".

        features -- if a string, builds a Modifier with only a feature
        """

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
        
    
        