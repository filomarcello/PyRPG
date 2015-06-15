'''
Created on 06/apr/2015

@author: marcello

This module contains classes useful for implementing a RPG character.
The base class, Character,  
'''

class Character(object): # TODO getters and setters
    '''Base class for a RPG character.
    
    This class implements a simple character having name, hitpoints, and
    experience points as minimal properties.
    '''
    
    def __init__(self, name: str = 'noname', 
                 xp: 'Number' = 0, 
                 hp: 'Number' = 1):
        '''Name, experience points and hitpoints make a basic RPG character.
        
        Default constructor:
        >>> c = Character()
        >>> print(c)
        Character: noname
        Xp: 0
        Hitpoints: 1
        
        >>> p = Character(name='Pippo', xp=1000, hp=20)
        >>> print(p)
        Character: Pippo
        Xp: 1000
        Hitpoints: 20
        '''
        
        self.name = name
        self.xp = xp # experience points
        self.hp = hp # hitpoints
    
    def __str__(self):
        return 'Character: {s.name}\nXp: {s.xp}\nHitpoints: {s.hp}'\
            .format(s=self)
                
        
class RPGCharacter(Character): # TODO 
    '''A complete RPG character.
    
    This class implements a RPG character with her/his name, race, attributes, 
    actions, inventory.
    To be added:
    - actions
    - history
    - race
    - occupation (RPG class)
    - attributes
    - inventory
    '''
    pass 

# testing by doctest         
if __name__ == "__main__":
    import doctest
    doctest.testmod() 