import unittest

from items.constants import CURRENCIES_EXCHANGE, DD_CURRENCIES
from items.treasure import Money

# dict for money with 100 copper, 5 silver, 2 electrum, 10 gold, 5 platinum
WALLET1 = {c: a for c, a in zip(DD_CURRENCIES, (5, 10, 5, 10, 100))}

# calculate the value of WALLET1 in gold coins
WALLET1_VALUE = sum([WALLET1[c] * exc for c, exc in
                     zip(DD_CURRENCIES, CURRENCIES_EXCHANGE)])


class TestMoney(unittest.TestCase):

    def setUp(self):

        self.m1 = Money()
        self.m2 = Money(WALLET1)
        self.m3 = Money({'gold': 28})

    def test_coins(self):

        self.assertEqual(self.m1.coins('copper'), 1)

        for c in self.m2.coins().keys():
            self.assertEqual(self.m2.coins(c), WALLET1[c])

        self.assertEqual(self.m1.coins('gold'), 0)
        self.assertEqual(self.m2.coins('gold'), 10)
        self.assertEqual(self.m3.coins('gold'), 28)
        self.assertEqual(self.m3.coins('copper'), 0)

    def test_value(self):

        self.assertEqual(self.m1.value(), 0.01)
        self.assertEqual(self.m2.value(), WALLET1_VALUE)
        self.assertEqual(self.m3.value(), 28)


if __name__ == '__main__':
    unittest.main()
