import unittest

from rpg_tools.dices import Dice, DiceTable

RETURNED =      ('two',    'six',     'five',   'one',   'four',   'three')
THROWS =        (2,        6,         5,        1,       4,        3)
INTERVALS_INT = ([11, 50], [96, 100], [81, 95], [1, 10], [61, 80], [51, 60])

SINGLE_THROW = list(zip(THROWS, RETURNED))
MINMAX_INT = list((*i, r) for i, r in zip(INTERVALS_INT, RETURNED))


class TestDice(unittest.TestCase):

    def setUp(self):

        self.d1 = Dice()
        self.d2 = Dice('3d8')
        self.d3 = Dice('4d12')
        self.d4 = Dice('5d6')

    def test_dice_values(self):

        self.assertEqual(self.d1.__str__(), '1d6')
        self.assertEqual(self.d2.__str__(), '3d8')

        self.assertGreaterEqual(self.d1.throw(), 1)
        self.assertLessEqual(self.d1.throw(), 6)

        self.assertGreaterEqual(self.d2.throw(), 3)
        self.assertLessEqual(self.d2.throw(), 24)

    def test_dice_sequences(self):

        self.assertEqual(self.d3.throw(), sum(self.d3.sequence))

        # checks if throw_this leaves sequence empty
        self.d4.throw_this('3d6')
        self.assertListEqual(self.d4.sequence, [])


class TestDiceTab(unittest.TestCase):

    def setUp(self):

        self.dt1 = DiceTable(SINGLE_THROW)
        self.dt2 = DiceTable(MINMAX_INT)
        # self.dt3 = DiceTable()

    def test_dicetable_single_throw(self):

        self.assertIn(self.dt1.throw(), RETURNED)
        self.assertSequenceEqual(self.dt1._breakpoints, sorted(THROWS))


    def test_dicetable_minmax_int(self):

        self.assertIn(self.dt2.throw(), RETURNED)
        self.assertSequenceEqual(self.dt2._breakpoints,
                                 sorted(ma for mi, ma in INTERVALS_INT))

    def test_dicetable_minmax_str(self):

        pass


if __name__ == '__main__':
    unittest.main()
