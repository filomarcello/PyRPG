import unittest
from characters.attributes import Abilities, DD_Abilities
from characters.constants import DD_ABILITIES_NAMES

AB = {'wisdom': 20, 'intelligence': 25}
ABB = {'bright': 10, 'telepathy': True, 'fading': 0.5}
DDAB = [12, 13, 14, 15, 16, 17]
DDABB = [15, 13, 14, 17, 9, 4]


class TestAttribute(unittest.TestCase):

    def setUp(self):
        self.ab1 = Abilities()
        self.ab2 = Abilities(AB)
        self.ab3 = Abilities(ABB)

        self.DDab1 = DD_Abilities()
        self.DDab2 = DD_Abilities(DDAB)
        self.DDab3 = DD_Abilities(DDABB)


    def test_default_abilities(self):
        self.assertEqual(self.ab1.get_ability('attack'), 1)

        for a in DD_ABILITIES_NAMES:
            self.assertEqual(self.DDab1.get_ability(a), 0)

    def test_custom_abilities(self):
        self.assertEqual(self.ab2.get_ability('wisdom'), 20)
        self.assertEqual(self.ab2.get_ability('intelligence'), 25)

        for a, v in zip(DD_ABILITIES_NAMES, DDAB):
            self.assertEqual(self.DDab2.get_ability(a), v)

    def test_set_ability(self):
        self.ab3.set_ability('bright', 25)
        self.assertEqual(self.ab3.get_ability('bright'), 25)

        self.ab3.set_ability('telepathy', False)
        self.assertFalse(self.ab3.get_ability('telepathy'))

        self.ab3.set_ability('fading', 0.98)
        self.assertAlmostEqual(self.ab3.get_ability('fading'), 0.98)

        self.DDab3.set_ability('strenght', 6)
        self.assertEqual(self.DDab3.get_ability('strenght'), 6)


if __name__ == '__main__':
    unittest.main()
