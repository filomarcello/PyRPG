'''
Created on 06/apr/2015

@author: marcello
'''

class Character(object):
    '''Base class for a RPG character.
    
    This class implements a simple character having name, hitpoints, and
    experience points as minimal properties.
    
    >>> c = Character(name='Pippo', xp=1000, hp=20)
    >>> print(c)
    Character: Pippo
    Xp: 1000
    Hitpoints: 20
    
    '''
    
    def __init__(self, name: str = 'Character', 
                 xp: 'Number' = 0, 
                 hp: 'Number' = 1):
        
        self.name = name
        self.xp = xp
        self.hp = hp
    
    def __str__(self):
        return 'Character: {s.name}\nXp: {s.xp}\nHitpoints: {s.hp}'\
            .format(s=self)
                
                
        
        
class RPGCharacter(Character): # TODO
    '''A minimal but complete RPG character.
    
    This class implements a RPG character with her/his name, race, attributes, 
    actions, inventory.
    Added until now:
    - actions
    '''
    pass 

# testing by doctest         
if __name__ == "__main__":
    import doctest
    doctest.testmod() 