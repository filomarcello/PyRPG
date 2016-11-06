""" created 06/11/2016
author: marcello
version: 0.1
"""
import time

from rpg_tools.dices import DiceTable

RETURNED =      ('two',    'six',     'five',   'one',   'four',   'three')
THROWS =        (2,        6,         5,        1,       4,        3)
INTERVALS_INT = ([11, 50], [96, 100], [81, 95], [1, 10], [61, 80], [51, 60])

SINGLE_THROW = list(zip(THROWS, RETURNED))
MINMAX_INT = list((*i, r) for i, r in zip(INTERVALS_INT, RETURNED))


dt1 = DiceTable(SINGLE_THROW)
dt2 = DiceTable(MINMAX_INT)
dt3 = DiceTable()

print('Single throw')
print(dt1._breakpoints, dt1._returned, dt1._cast_times, dt1._faces)

for i in range(10):
    print(dt1.throw(), end=' ')
    time.sleep(0.1)

print('\n\nIntervals')
print(dt2._breakpoints, dt2._returned, dt2._cast_times, dt2._faces)

for i in range(10):
    print(dt2.throw(), end=' ')
    time.sleep(0.1)