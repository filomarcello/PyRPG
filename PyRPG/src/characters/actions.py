'''
Created on 21/apr/2015

@author: marcello
'''

class Actions(object):
    '''Base class for RPG character actions.
    
    This class implements only the movement action.Actions.
    '''
    
    def __init__(self, actions: dict = {'movement': 1):
        '''Implements only the action movement.
        
        Actions:            Default:            Units:
        - movement:         1                   distance unit per turn
        '''
        
        self.actions = actions
    
    