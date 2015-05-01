'''
Created on 23/apr/2015

@author: marcello
'''

class Modifier(object):
    '''Class that maps modifiers onto the actions.
    
    This class should be considered as a dict with actions names as keys and 
    values as relative numbers to be added to the character action.
    Each item, ability or whatever has a Modifier class. The character class
    will manage them.    
    '''

    def __init__(self, actions: 'Actions'):
        '''Build an empty Modifiers with Actions names.
        
        '''
        self.modifiers = {k: 0 for k in actions.keys}
        
    def add(self, name: str, value: 'Number'):    
        '''Add the modifier value to the name action.'''
        self.modifiers[name] = value
        