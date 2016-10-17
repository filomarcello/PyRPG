import unittest
from items.container import Container
from items.item import Item

ITEM = Item(name='pot', weight=500)

CUSTOM_ITEMS = [Item(name='rope', weight=2500),
                Item(name='knife', weight=100),
                Item(name='bottle', weight=1000)]

CUSTOM_ITEMS_2 = [Item(name='rope', weight=2500),
                Item(name='knife', weight=100),
                Item(name='bottle', weight=1000)]

CUSTOM_ITEMS_3 = [Item('gem', weight=10),
                  Item('staff', weight=1000),]


class TestContainer(unittest.TestCase):

    def setUp(self):

        self.c1 = Container(name='sack', weight=100,
                            items=[ITEM,])
        self.c2 = Container(name='backpack', weight=1000,
                            items=CUSTOM_ITEMS)
        self.c3 = Container()

        self.c4 = Container(name='bag', weight=50,
                            items=CUSTOM_ITEMS_2)


    def test_weight(self):

        self.assertEqual(self.c1.weight, 600)
        self.assertEqual(self.c2.weight, 4600)


    def test_inplace_operators(self):

        # default container plus an item
        self.c3 += ITEM
        self.assertEqual(self.c3.weight, ITEM.weight)

        self.c3 -= ITEM
        self.assertEqual(self.c3.weight, 0)

        self.c3 += CUSTOM_ITEMS_3
        self.assertEqual(len(self.c3._items), 2)
        self.assertEqual(self.c3.weight, 1010)

        self.c3 += ITEM
        self.c3 -= CUSTOM_ITEMS_3
        self.assertEqual(len(self.c3._items), 1)
        self.assertEqual(self.c3.weight, ITEM.weight)

        self.c4 += ITEM
        self.assertEqual(self.c4.weight, 4150)


    def test_name(self):

        self.c3.name = 'portfolio'
        self.assertEqual(self.c3.name, 'portfolio')


if __name__ == '__main__':
    unittest.main()
