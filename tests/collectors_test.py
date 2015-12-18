import unittest
from items.collectors import ItemCollector
from items.item import Item


it1 = Item(name='rope', weight=1.0)
it2 = Item(name='scroll', weight=0.05)
it3 = Item(name='sword', weight=3.0)
it4 = Item(name='axe', weight=2.0)
it5 = Item(name='knife', weight=0.5)

its = [it3, it4, it5]


class TestItemCollector(unittest.TestCase):

    def setUp(self):
        self.collector = ItemCollector(items=its)
        self.collector2 = ItemCollector(items=[it1, it5])

    def test_weight(self): # and also test for add and iadd operator overload

        self.assertEqual(self.collector.weight, 5.5)
        self.collector = self.collector + it1
        self.assertEqual(self.collector.weight, 6.5)
        self.collector += it2
        self.assertEqual(self.collector.weight, 6.55)

        self.collector = self.collector - it1
        self.assertEqual(self.collector.weight, 5.55)

        self.collector -= it3
        self.assertEqual(self.collector.weight, 2.55)

    def test___contains__(self):

        self.assertTrue(it1 in self.collector2)
        self.assertFalse(it2 in self.collector2)


if __name__ == '__main__':
    unittest.main()
