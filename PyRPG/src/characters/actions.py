"""
Created on 21/apr/2015

@author: marcello

Modified 04/11/2016: implemented as a single action
"""

class Action(object):
    """Base class for RPG character action.

    Actions are movement, melee attack, range attack, infravision, and so on.
    """
    
    def __init__(self, name: str, value):
        """name -- name of the action."""
        self._name = name

    # properties

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name


