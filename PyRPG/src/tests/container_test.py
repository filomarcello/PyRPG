import unittest
from items.container import Container, Backpack
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

CUSTOM_ITEMS_4 = [Item(name='gem', weight=10),
                  Item(name='flask', weight=50),
                  Item(name='button', weight=2),
                  Item(name='book', weight=150),
                  Item(name='stone', weight=1000)]


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


class TestBackpack(unittest.TestCase):

    def setUp(self):

        self.b1 = Backpack(weight=50, max_items=5, max_weight=None)
        self.b2 = Backpack(weight=25, max_items=None, max_weight=1000)

    def test_weight(self):

        self.assertEqual(self.b1.weight, 50)
        self.assertEqual(self.b2.weight, 25)

    def test_inplace_operators(self):

        # test max number of items capacity
        self.b1 += CUSTOM_ITEMS_2 # +3
        self.b1 += ITEM # +1
        self.b1 += CUSTOM_ITEMS_4 # +4 (too much)
        self.assertEqual(len(self.b1.items), 4) # remaining 4

        # test max weight capacity
        self.b2 += ITEM # +500
        self.b2 += ITEM # +500
        self.b2 += CUSTOM_ITEMS # + a lot
        self.assertEqual(len(self.b2.items), 2) # remaining 2 (weight = 1000)

if __name__ == '__main__':
    unittest.main()
