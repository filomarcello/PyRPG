'''
Created on 01/mag/2015

@author: marcello
'''
import random as rand
import itertools as itools
import bisect as bs

class Dice(object):
    '''Implements the classical dices in RPG.
    
    Usually d6, d8, d10 and so on.   
    '''
    
    def __init__(self, dice_string: str = 'd6'):
        '''Uses the typical RPG code as a string to build a dice.
        
        It does not check if dice_string is a valid dice code.
        The default dice is the common cube: d6 (or 1d6)
        >>> d = Dice()
        >>> print(d)
        1d6
         
        >>> d2 = Dice('3d8')
        >>> print(d2)
        3d8
        
        Assert 'd' in dice_string. TODO Exceptions?
        '''
        self._cast_times, self._faces = self._process_dice_string(dice_string)
        self._sequence =  [] # stores the sequence of numbers thrown
        
    def __str__(self):
        return str(self._cast_times) + 'd' + str(self._faces)
    
    def throw(self) -> int:
        '''Dice is thrown.
        
        >>> d = Dice('3d8')
        >>> 3 <= d.throw() <= 24
        True
        '''
        self._sequence = self._throws(self._cast_times, self._faces)
        return sum(self._sequence)
    
    def get_sequence(self) -> list:
        '''Returns the list values generated during throw function call.
        
        >>> d = Dice('5d20')
        >>> o = d.throw()
        >>> sum(d.get_sequence()) == o
        True
        '''
        return self._sequence
    
    def throw_this(self, dice_string: str) -> int:
        '''Static method that throws a temporary whatever dice.
        
        Does not hold faces, cast_times, and sequences. For this purpose build
        a proper dice by constructor.
        >>> d = Dice()
        >>> print(d)
        1d6
        >>> 3 <= d.throw_this('3d10') <= 30
        True
        '''
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
    '''Implements a table of intervals to select randomly.'''
    
    def __init__(self, tab: tuple): 
        '''tab is a tuple from which random weighted select an item.
        
        tab has to be as the following:
        ((weight, item_to_return), ...)
                
        >>> dt = DiceTable(((1, 'one'), (2, 'two'), (9, 'else')))
        >>> dt._faces
        12
        >>> dt._cumul
        (1, 3, 12)
        >>> dt._items
        ('one', 'two', 'else')
        '''
        weights, items = list(zip(*tab))
        super().__init__('1d' + str(sum(weights)))
        self._cumul = tuple(itools.accumulate(weights))
        self._items = items
        
    def throw(self):
        '''Returns random weighted item.
        
        >>> dt = DiceTable(((1, 'one'), (4, 'two'), (5, 'else')))
        >>> dt.throw() in ['one', 'two', 'else']
        True
        '''
        return self._items[bs.bisect(self._cumul, super().throw())]
    
# tests

if __name__ == '__main__':
    import doctest
    doctest.testmod()