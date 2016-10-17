"""
Created on 20/apr/2015
modified: 31/08/2016 - rewrited tests (unittest)

@author: marcello
"""

from characters.constants import DD_ABILITIES_NAMES

class Abilities(object):
    """Base class for ability scores.

    Wraps a dictionary being keys the name of the abilities and values
    the scores. The scores must be numbers, whatever type.
    """

    def __init__(self, abilities: dict = {'attack': 1}):
        """Creates an object with a dict of abilities."""

        self._abilities = abilities
        
    def set_ability(self, ability_name: str, value):
        """Set the ability_name to the value."""

        self._abilities[ability_name] = value
        
    def get_ability(self, ability_name: str):
        """Get the value of 'ability_name'."""

        return self._abilities[ability_name]
    

class DD_Abilities(Abilities):
    """Set then abilities to the standard D&D.

    Preset abilities are strength, dexterity, constitution, intelligence,
    wisdom, and charisma.
    """
    
    def __init__(self, values: list = [0, 0, 0, 0, 0, 0]):
        """Order of the values list: str, dex, con, int, wis, cha.

        Default are zero values."""

        super().__init__(abilities={n: v for n, v 
                                    in zip(DD_ABILITIES_NAMES, values)})
                                    
