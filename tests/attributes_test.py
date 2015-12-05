import unittest
from characters.attributes import Attributes, DDattributes
from characters.attributes import STR, DEX, CON, INT, WIS, CHA


class AttributesTest(unittest.TestCase):

    def setUp(self):
        self.attribute = Attributes(attributes={'strength':12,
                                                'intelligence':14})
        self.DDAttr = DDattributes()

    def test_attribute(self):

        # tests base Attributes class
        self.assertEqual(self.attribute.get_attribute(name='strength'), 12)
        self.assertEqual(self.attribute.get_attribute(name='intelligence'), 14)
        self.attribute.set_attribute(name='strength', value=18)
        self.assertEqual(self.attribute.get_attribute(name='strength'), 18)

        # tests DDattributes class
        self.assertEqual(self.DDAttr.get_attribute(STR), 0)
        self.assertEqual(self.DDAttr.get_attribute(DEX), 0)
        self.assertEqual(self.DDAttr.get_attribute(CON), 0)
        self.assertEqual(self.DDAttr.get_attribute(INT), 0)
        self.assertEqual(self.DDAttr.get_attribute(WIS), 0)
        self.assertEqual(self.DDAttr.get_attribute(CHA), 0)


if __name__ == '__main__':
    unittest.main()
