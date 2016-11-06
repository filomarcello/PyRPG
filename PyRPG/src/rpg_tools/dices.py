"""
Created on 01/mag/2015

@author: marcello
"""
import random as rand
import itertools as itools
import bisect as bs

class Dice(object):
    """Implements the classical dices in RPG.

    Usually d6, d8, d10 and so on.
    """
    
    def __init__(self, dice_string: str = 'd6'):
        """Uses the typical RPG code as a string to build a dice.

        It does not check if dice_string is a valid dice code.
        The default dice is the common cube: d6 (or 1d6).
        """
        self._cast_times, self._faces = self._process_dice_string(dice_string)
        self._sequence =  [] # stores the sequence of numbers thrown
        
    def __str__(self):
        return str(self._cast_times) + 'd' + str(self._faces)
    
    def throw(self) -> int:
        """Dice is thrown."""
        self._sequence = self._throws(self._cast_times, self._faces)
        return sum(self._sequence)

    @property
    def sequence(self) -> list:
        """Returns the list values generated during throw function call."""
        return self._sequence
    
    def throw_this(self, dice_string: str) -> int:
        """Static method that throws a temporary whatever dice.

        Does not hold faces, cast_times, and sequences. For this purpose build
        a proper dice by constructor.
        """
        return sum(self._throws(*self._process_dice_string(dice_string)))
    
    # internal function that processes dice_string    
    def _process_dice_string(self, dice_string: str) -> tuple:
        # times to throw the dice
        cast_times = dice_string[:dice_string.find('d')] or 1
        cast_times = int(cast_times)
        # number of the dice faces
        faces = int(dice_string[dice_string.find('d') + 1:])
        return cast_times, faces
    
    # internal function that throws a sequence of dice casts
    def _throws(self, cast_times, faces):
        return [rand.randint(1, faces) 
                for i in range(cast_times)]
    
    
class DiceTable(Dice):
    """Implements a table of intervals to select randomly.

    Frequently in RPG games events, wandering monsters, treasures, etc. were
    determined by a dice throw and a reference table. E.g 1 to 5: goblins,
    6 to 13: cobolds, 14 to 20: hobgoblins.

    DiceTable extends a single dice (1dX) being X the maximum of the last
    interval.
    """
    
    def __init__(self, tab: list):
        """tab -- a list of tuples.

        Each tuple can be:
        - (throw, returned): throw is the precise number of dice throw.
        - (min, max, returned): min and max are boundaries of the interval.
        - ('min-max', returned): min-max is a string with interval boundaries
        Returned is what has to be returned in corrispondence of that result.

        Doesn't check the integrity of intervals and data.
        """
        if len(tab[0]) == 2: # (throw, returned)
            tab.sort()

            # the first element of the last tuple is the maximum
            super().__init__('1d' + str(tab[-1][0]))

            self._table = tuple(tab)


        # if len(tab[0]) == 3: # (min, max, returned)
        #     mins, maxs, items = zip(*tab)
        #
        #     # initialize a dice with number of faces == max of the maximi of the
        #     # intervals
        #     super().__init__('1d' + str(max(maxs)))

            # weights, items = list(zip(*tab))
            #
            # self._cumul = tuple(itools.accumulate(weights))
            # self._items = items
        
    def throw(self):
        """Returns random item in the table."""
        return rand.choice(self._table)[1]

