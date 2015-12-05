""" created 16/11/15
author: marcello
"""

# from characters.constants import STR, DEX, CON, INT, WIS, CHA
from constants.constants import DD_ATTRIBUTES


class Attributes:
    """Wraps the attributes of a character.

    E.g. strength, constitution, and so on."""

    def __init__(self, attributes: dict):
        """attributes is a dictionary.

        Name of the attributes as keys and their values.
        E.g {'strenght':12, 'charisma':18, ...}
        """

        self._attributes = attributes

    def get_attribute(self, name: str):
        return self._attributes[name]

    def set_attribute(self, name: str, value):
        self._attributes[name] = value


class DDattributes(Attributes):
    """Classic D&D or AD&D RPG attributes."""

    def __init__(self):
        """Builds D%D attributes with 0 (zero) values."""
        super().__init__(attributes=dict(zip(DD_ATTRIBUTES, (0, 0, 0, 0, 0, 0))))