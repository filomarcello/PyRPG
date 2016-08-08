"""Testing Item and Item subclasses: Container."""

import unittest
from items.item import Item
from items.container import Container


class TestItem(unittest.TestCase):

    def setUp(self):

        self.i1 = Item()
        self.i2 = Item(name='axe', weight=1000)

        self.c1 = Container()
        self.c2 = Container(name='backpack', weight=2000)

    def test_default_item(self):

        self.assertEqual(self.i1.name, 'item')
        self.assertEqual(self.i1.weight, 0)

        self.assertEqual(self.c1.name, 'container')
        self.assertEqual(self.c1.weight, 0)


    def test_custom_item(self):

        self.assertEqual(self.i2.name, 'axe')
        self.assertEqual(self.i2.weight, 1000)

        self.assertEqual(self.c2.name, 'backpack')
        self.assertEqual(self.c2.weight, 2000)


    def test_properties_item(self):

        self.i2.name = 'battleaxe'
        self.assertEqual(self.i2.name, 'battleaxe')
        self.i2.weight = 3000
        self.assertEqual(self.i2.weight, 3000)

        self.c2.name = 'jetpack'
        self.assertEqual(self.c2.name, 'jetpack')
        self.c2.weight = 500
        self.assertEqual(self.c2.weight, 500)


if __name__ == '__main__':
    unittest.main()
