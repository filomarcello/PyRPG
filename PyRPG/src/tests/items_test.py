import unittest
from items.item import Item


class TestItem(unittest.TestCase):

    def setUp(self):

        self.i1 = Item()
        self.i2 = Item(name='axe', weight=10.5)


    def test_default_item(self):

        self.assertEqual(self.i1.name, 'item')
        self.assertEqual(self.i1.weight, 0.0)


    def test_custom_item(self):

        self.assertEqual(self.i2.name, 'axe')
        self.assertEqual(self.i2.weight, 10.5)


    def test_properties_item(self):

        self.i2.name = 'battleaxe'
        self.assertEqual(self.i2.name, 'battleaxe')
        self.i2.weight = 20.0
        self.assertEqual(self.i2.weight, 20.0)


if __name__ == '__main__':
    unittest.main()
