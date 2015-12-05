import unittest
from items.item import Item, RPGItem

MODS = {'attack': 1, 'speed': -1, 'luck': True}

class ItemTest(unittest.TestCase):

    def setUp(self):
        self.item = Item(name='axe', weight=12.5)

    def test_name(self):
        self.assertEqual(self.item.name, 'axe')
        self.item.name = 'sword'
        self.assertEqual(self.item.name, 'sword')

    def test_weight(self):
        self.assertEqual(self.item.weight, 12.5)
        self.item.weight = 10.0
        self.assertEqual(self.item.weight, 10.0)

class RPGItemTest(unittest.TestCase):

    def setUp(self):
        self.RPGitem = RPGItem(name='sword', weight=5.0, mods=MODS)

    def test_name(self):
        self.assertEqual(self.RPGitem.name, 'sword')
        self.RPGitem.name = 'long sword'
        self.assertEqual(self.RPGitem.name, 'long sword')

    def test_weight(self):
        self.assertEqual(self.RPGitem.weight, 5.0)
        self.RPGitem.weight = 10.0
        self.assertEqual(self.RPGitem.weight, 10.0)

    def test_get_mod(self):
        self.assertEqual(self.RPGitem.get_mod('attack'), 1)
        self.assertEqual(self.RPGitem.get_mod('speed'), -1)

    def test_set_mod(self):
        self.RPGitem.set_mod('attack', 2)
        self.assertEqual(self.RPGitem.get_mod('attack'), 2)

        self.RPGitem.set_mod('foo', 18)
        self.assertEqual(self.RPGitem.get_mod('foo'), 18)

    def test_get_modifiers(self):
        self.assertEqual(self.RPGitem.get_modifiers(), MODS)


if __name__ == '__main__':
    unittest.main()
