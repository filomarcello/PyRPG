import unittest
from meta.modifier import Modifier
from constants.constants import DEX, HP, DAM

MODS = {DEX:2, HP:1, DAM:-1}

class ModifierTest(unittest.TestCase):

    def setUp(self):
        self.mod = Modifier(MODS)

    def test_get_mod(self):
        self.assertEqual(self.mod.get_mod(DEX), 2)
        self.assertEqual(self.mod.get_mod(HP), 1)
        self.assertEqual(self.mod.get_mod(DAM), -1)

    def test_set_mod(self):
        self.mod.set_mod(DEX, -1)
        self.assertEqual(self.mod.get_mod(DEX), -1)

        self.mod.set_mod('foo', 18)
        self.assertEqual(self.mod.get_mod('foo'), 18)

    def test_get_modifiers(self):
        self.assertEqual(self.mod.get_modifiers(), MODS)


if __name__ == '__main__':
    unittest.main()
