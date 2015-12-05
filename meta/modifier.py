""" created 29/11/2015
author: marcello
"""

class Modifier:
    """Modifier class is a layer of values applied to other parameters.

    """ # TODO: more explanation and examples

    def __init__(self, mods: dict = {}):
        self._mods = mods


    def get_mod(self, name: str):
        """Returns the 'name' modifier."""
        return self._mods.get(name)

    def get_modifiers(self):
        """Returns all the modifiers."""
        return self._mods

    def set_mod(self, name: str, value):
        self._mods[name] = value

