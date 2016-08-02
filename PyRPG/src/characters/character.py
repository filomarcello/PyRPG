"""
Created on 06/apr/2015
Modified: 02/08/2016: added level, tests remade

@author: marcello

This module contains classes useful for implementing a RPG character.
The base class, Character, and the extended RPGCharacter.
"""

class Character(object):
    '''Base class for a RPG character.
    
    This class implements a simple character having name, hitpoints, and
    experience points as minimal properties.
    '''
    
    def __init__(self, name: str = 'noname', 
                 xp: 'Number' = 0, 
                 hp: 'Number' = 1,
                 level: 'Number' = 1):
        """Name, XPs, level and hitpoints make a basic RPG character."""
        
        self._name = name
        self._xp = xp # experience points
        self._hp = hp # hitpoints
        self._level = level

    def __str__(self):
        return 'Character: {s._name}\nXp: {s._xp}\nHitpoints: {s._hp}\
            \nLevel: {s._level}'.format(s=self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, xp):
        self._xp = xp

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp
                
        
class RPGCharacter(Character): # TODO 
    """A complete RPG character.

    This class implements a RPG character with her/his name, race, attributes,
    actions, inventory.
    To be added:
    - actions
    - history
    - race
    - occupation (RPG class)
    - attributes
    - inventory
    """
    pass 

