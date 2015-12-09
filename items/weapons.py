""" created 05/12/2015
author: marcello
"""

from constants.constants import DAM
from items.item import RPGItem

class Weapon(RPGItem):
    """Base class for weapons."""

    def __init__(self, name: str = 'weapon',
                 weight: float = 0.0,
                 mods: dict = {}):

        super().__init__(name, weight, mods)

    def __str__(self):
        return 'Weapon:{s._name}, weight:{s._weight}'.format(s=self)


class MeleeWeapon(Weapon):
    """Base class for melee weapons."""

    def __init__(self, name: str = 'melee weapon',
                 weight: float = 0.0,
                 mods: dict = {},
                 damage=1):

        super().__init__(name, weight, mods)
        self._damage = damage

    def __str__(self):
        return super().__str__() + ', damage:{s._damage}'.format(s=self)


    def get_damage(self):
        return self._damage + self.get_mod(DAM) # TODO: get mods from damage?

