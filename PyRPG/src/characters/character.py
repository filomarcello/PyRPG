'''
Created on 06/apr/2015

@author: marcello
'''

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
        