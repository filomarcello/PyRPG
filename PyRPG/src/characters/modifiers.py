'''
Created on 23/apr/2015

@author: marcello
'''

class Modifier(object):
    '''Class that map modifiers from abilities, races, etc. to actions.'''

    def __init__(self, mod_tableau: 'URI'):
        '''Builds a modifier reading a file of modificators in URI pathway.
        
        The file must be in csv format (',' as separator
        '''
        