'''
Created on 16/mag/2015

@author: marcello
'''

import csv

class TableLoader(object):
    '''Tool useful for load tables from files.
    
    The file must to have csv format with:
    - first row as field names
    - ',' as separator
    - no "" delimiters.
    
    E.g. a csv file for class abilities minimums
    
    class,strenght,dexterity,constitution,intelligence,wisdom,charisma
    fighter,9,0,0,0,0,0
    paladin,12,0,9,0,13,17
    ...
    '''
    def __init__(self, file):
        '''file has to be a path to a csv file.
        
        TODO TESTS
        '''
        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile)
        
        
        


if __name__ == '__main__':
    import doctest
    doctest.testmod()