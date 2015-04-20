'''
Created on 20/apr/2015

@author: marcello
'''

class Abilities(object):
    '''Base class for ability scores.
    
    Wraps a dictionary being keys the name of the abilities and values
    the scores.
    '''

    def __init__(self, abilities: dict = {'strength': 1}):
        self.abilities = abilities
        