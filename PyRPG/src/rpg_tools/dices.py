'''
Created on 01/mag/2015

@author: marcello
'''
import random as rand

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
        
        # times to throw the dice
        self._cast_times = dice_string[:dice_string.find('d')] or 1
        self._cast_times = int(self._cast_times)
        
        # number of the dice faces
        self._faces = int(dice_string[dice_string.find('d') + 1:])
        
        self._sequence =  [] # stores the sequence of numbers thrown
        
    def __str__(self):
        return str(self._cast_times) + 'd' + str(self._faces)
    
    def throw(self) -> int:
        '''Dice is thrown.
        
        >>> d = Dice('3d8')
        >>> 3 <= d.throw() <= 24
        True
        '''
        
        self._sequence = [rand.randint(1, self._faces) 
                          for i in range(self._cast_times)]
        
        return sum(self._sequence)
    
    def get_sequence(self) -> list:
        '''Returns the list values generated during throw function call.
        
        >>> d = Dice('5d20')
        >>> o = d.throw()
        >>> sum(d.get_sequence()) == o
        True
        '''
        return self._sequence    
    
# tests
if __name__ == '__main__':
    import doctest
    doctest.testmod()