import unittest
from collections import Counter

from items.constants import CURRENCIES_EXCHANGE, DD_CURRENCIES
from items.treasure import Money


TUPLE_COINS = (10, 5, 1, 1, 0)
LIST_COINS = [100, 7, 4, 1, 1]

WALLET1 = {'copper': 100, 'silver': 10, 'electrum': 5, 'gold': 10, 'platinum': 5}
WALLET2 = {'copper': 50, 'silver': 5, 'electrum': 2, 'gold': 2, 'platinum': 1}

# calculate the value of WALLET1 in gold coins
WALLET1_VALUE = sum([WALLET1[c] * exc for c, exc in
                     zip(DD_CURRENCIES, CURRENCIES_EXCHANGE)])


class TestMoney(unittest.TestCase):

    def setUp(self):

        self.m1 = Money() # empty constructor
        self.m2 = Money(WALLET1) # complete dict
        self.m3 = Money({'gold': 28}) # partial dict
        self.m4 = Money(TUPLE_COINS) # tuple
        self.m5 = Money(LIST_COINS) # list
        self.m6 = Money(**WALLET2)# complete kwargs
        self.m7 = Money(copper=50, gold=8) # partial kwargs

    def test_coins(self):

        for c in DD_CURRENCIES:
            self.assertEqual(self.m1.coins(c), 0)

        for c in self.m2.coins().keys():
            self.assertEqual(self.m2.coins(c), WALLET1[c])

        self.assertEqual(self.m3.coins('copper'), 0)
        self.assertEqual(self.m3.coins('silver'), 0)
        self.assertEqual(self.m3.coins('electrum'), 0)
        self.assertEqual(self.m3.coins('gold'), 28)
        self.assertEqual(self.m3.coins('platinum'), 0)

        for c, v in zip(DD_CURRENCIES, TUPLE_COINS):
            self.assertEqual(self.m4.coins(c), v)

        for c, v in zip(DD_CURRENCIES, LIST_COINS):
            self.assertEqual(self.m5.coins(c), v)

        for c, v in WALLET2.items():
            self.assertEqual(self.m6.coins(c), v)

        self.assertEqual(self.m7.coins('copper'), 50)
        self.assertEqual(self.m7.coins('silver'), 0)
        self.assertEqual(self.m7.coins('electrum'), 0)
        self.assertEqual(self.m7.coins('gold'), 8)
        self.assertEqual(self.m7.coins('platinum'), 0)


    def test_value(self):

        # self.assertEqual(self.m1.value(), 0.01)
        # self.assertEqual(self.m2.value(), WALLET1_VALUE)
        # self.assertEqual(self.m3.value(), 28)
        pass

    def test_weight(self):
        pass

if __name__ == '__main__':
    unittest.main()
