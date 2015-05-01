'''
Created on 21/apr/2015

@author: marcello
'''

class Actions(object):
    '''Base class for RPG character actions.
    
    Actions are movement, melee attack, range attack and so on.
    '''
    
    def __init__(self, actions: dict = {'movement': 1}):
        '''By default implements only the action movement.
        
        Default constructor
        >>> a = Actions()
        >>> a.get_action('movement')
        1
        '''
        self._actions = actions
        
    def get_action(self, action_name):
        '''Returns the value of the action_name.
        
        >>> a = Actions(actions={'movement': 12, 'attack': 1})
        >>> a.get_action('attack')
        1
        >>> a.get_action('movement')
        12
        '''
        return self._actions[action_name]
    
    def set_action(self, action_name, value):
        '''Sets the value of action_name.
        
        >>> a = Actions()
        >>> a.set_action('movement', 10)
        >>> a.get_action('movement')
        10
        '''
        self._actions[action_name] = value
    

# testing by doctest         
if __name__ == "__main__":
    import doctest
    doctest.testmod() 