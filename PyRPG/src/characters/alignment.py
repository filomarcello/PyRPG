'''
Created on 02/mag/2015

@author: marcello
'''

class Alignment(object):
    '''Implements the alignment of a RPG character.'''

    def __init__(self, ethics: str = 'neutral'):
        '''Ethics is to be intended as respect for the society's rules.
        
        Default is neutral. It does not implement other degrees of ethics.
        >>> a = Alignment()
        >>> print(a)
        Alignment: neutral
        '''
        self._ethics = ethics
        
    def __str__(self):
        return 'Alignment: ' + self._ethics
    
DD_ALIGN_LAWFUL  = 'lawful'
DD_ALIGN_NEUTRAL = 'neutral'
DD_ALIGN_CHAOTIC = 'chaotic'

class DD_Alignment(Alignment):
    '''Extends Alignment to D&D ones.
    
    May be: lawful, neutral, chaotic, and nothing else.
    '''

    def __init__(self, ethics: str = 'neutral'):
        '''Ethics is to be intended as respect for the society's rules.
        
        Default is neutral. TODO: use exceptions
        >>> a = DD_Alignment('lawful')
        >>> print(a)
        Alignment: lawful
        '''
        super().__init__(ethics)
        
    def is_lawful(self) -> bool:
        '''Checks if the alignment is lawful.
        
        >>> a = DD_Alignment('chaotic')
        >>> a.is_lawful()
        False
        '''
        return self._ethics == DD_ALIGN_LAWFUL
    
    def is_neutral(self) -> bool:
        '''Checks if the alignment is neutral.
        
        >>> a = DD_Alignment('chaotic')
        >>> a.is_neutral()
        False
        '''
        return self._ethics == DD_ALIGN_NEUTRAL
    
    def is_chaotic(self) -> bool:
        '''Checks if the alignment is chaotic.
        
        >>> a = DD_Alignment('chaotic')
        >>> a.is_chaotic()
        True
        '''
        return self._ethics == DD_ALIGN_CHAOTIC
    
    def get_alignment(self):
        '''Returns the alignment.
        
        >>> a = DD_Alignment('lawful')
        >>> a.get_alignment()
        'lawful'
        '''
        return self._ethics
    
    def set_alignment(self, ethics):
        '''Sets a new alignment.
        
        >>> a = DD_Alignment('lawful')
        >>> print(a)
        Alignment: lawful
        >>> a.set_alignment('chaotic')
        >>> print(a)
        Alignment: chaotic
        '''
        self._ethics = ethics

# TODO implements ADD_Alignments


# testing by doctest         
if __name__ == "__main__":
    import doctest
    doctest.testmod() 