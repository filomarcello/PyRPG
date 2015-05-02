'''
Created on 02/mag/2015

@author: marcello
'''

class SavingThrows(object):
    '''Implements saving throws in RPG game.'''

    def __init__(self, saving_throws: dict = {}):
        '''saving_trows parameter is a dict name: value.
        
        >>> test TODO
        '''
        
        self._saving_throws = saving_throws
        
    def check_saving_throw(self, name, throw):
        '''Evaluates if the saving throw 'name' is more than throw.
        
        If saving throw
        >>> test TODO
        '''
        return throw > self._saving_throws[name]