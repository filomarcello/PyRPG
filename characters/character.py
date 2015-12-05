""" created 16/11/15
author: marcello
"""

class Character:
    """Base class for a RPG character.

    This class implements a simple character having name, hitpoints, and
    experience points as minimal properties.
    """

    def __init__(self,
                 name: str = 'character',
                 xp: int = 0,
                 hp: int = 1):
        """Name, experience points and hitpoints make a basic RPG character."""

        self._name = name
        self._xp = xp # experience points
        self._hp = hp # hitpoints

    # properties

    @property
    def name(self):
        """Property of the name attribute."""
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def xp(self):
        """Property of experience points."""
        return self._xp

    @xp.setter
    def xp(self, xp: int):
        self._xp = xp

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp: int):
        self._hp = hp

    # methods
    def add_xp(self, xp: int):
        self._xp += xp

    def add_hp(self, hp: int):
        self._hp += hp

    # TODO needs subtract xp/hp?

    def __str__(self):
        return 'Character:{s.name}, XP:{s.xp}, HP:{s.hp}'.format(s=self)

class RPGCharacter(Character):
    """Base class for a general RPG character.

    RPGCharacter has attributes, class, and race more than Character class.
    """

    pass # TODO complete the class. Testing.


