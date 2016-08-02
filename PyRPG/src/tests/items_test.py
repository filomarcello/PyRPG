import unittest
from items.item import Item


class TestItem(unittest.TestCase):

    def setUp(self):
        self.item = Item(name='Axe', weight=10.5)

    def test_name(self):
        self.assertEqual(self.item.name, 'axe')
        self.item.name = 'sword'
        self.assertEqual(self.item.name, 'sword')

    # def test_weight(self):
    #     self.assertEqual(self.item.weight, 10.5)
    #     self.item.weight = 9.0
    #     self.assertEqual(self.item.weight, 9.0)


if __name__ == '__main__':
    unittest.main()
