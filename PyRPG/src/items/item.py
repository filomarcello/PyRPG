"""
Created on 05/apr/2015
Modified: 16/11/2015
          02/08/2016 revised tests

@author: marcello
"""


class Item:
    """Base abstract class for a generic item.

    All items have at least a name and a weight.
    """
    
    def __init__(self, name: str = 'item', weight: float = 0.0):
        """Absolutely generic item."""
        self._name = name
        self._weight = weight

    @property
    def weight(self):
        """Weight property of the Item."""
        return self._weight

    @weight.setter
    def weight(self, w: float):
        self._weight = w

    @property
    def name(self):
        """Name property of the Item."""
        return self._name

    @name.setter
    def name(self, n: str):
        self._name = n
        
    def __str__(self):
        return 'Item:{s._name}, Weight:{s._weight}'.format(s=self)


# class RPGItem(Item):
#     '''Extends the generic Item with modifier.'''
#
#     def __init__(self, name: str = 'noname',
#                  weight: float = 0.0,
#                  modifier: 'Modifier' = None,
#                  magic: bool = False):
#         '''modifier is a Modifier class containing modificators.
#
#         This class allow item modificators which will be managed by the
#         Character class.
#
#         >>> from characters.modifiers import Modifier
#         >>> from characters.actions import Actions
#         >>> i = RPGItem('thing', 1.0, Modifier(Actions()))
#         >>> print(i)
#         RPGItem: thing
#         Weight: 1.0
#         '''
#         super().__init__(name, weight)
#         self._modifier = modifier
#         self._magic = magic
#
#     def get_modifier(self):
#         '''Returns the modifiers associated with this item.'''
#         return self._modifier
#
#     def is_magic(self) -> bool:
#         return self._magic
#
#     def __str__(self):
#         return 'RPGItem: {s._name}\nWeight: {s._weight}'.format(s=self)
#
