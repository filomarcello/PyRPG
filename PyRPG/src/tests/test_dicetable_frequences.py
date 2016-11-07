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
dt3 = DiceTable([(96, 100, 'minor'), (1, 95, 'major')])

st = list(dt1.throw() for i in range(10000))
mm = list(dt2.throw() for i in range(10000))
asim = list(dt3.throw() for i in range(10000))

n_st = {r: st.count(r) for r in RETURNED}
n_mm = {r: mm.count(r) for r in RETURNED}
n_asim = {r: asim.count(r) for r in ('minor', 'major')}

print(n_st, n_mm, n_asim, sep='\n')