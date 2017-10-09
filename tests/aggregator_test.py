import unittest
from meta.aggregator import Aggregator
from constants.constants import DD_ATTRIBUTES, STR, INT

ATTRIBUTES_EMPTY = dict(zip(DD_ATTRIBUTES, (None,) * 6))
ATTRIBUTES_FULL = dict(zip(DD_ATTRIBUTES, (5,) * 6))


class AggregatorTest(unittest.TestCase):

    def setUp(self):
        self.a1 = Aggregator()
        self.a2 = Aggregator(DD_ATTRIBUTES)
        self.a3 = Aggregator(list(DD_ATTRIBUTES))
        self.a4 = Aggregator(ATTRIBUTES_EMPTY)
        self.a5 = Aggregator(ATTRIBUTES_FULL)

    def test_blank_constructor(self):
        self.assertDictEqual(self.a1.properties, {})

    def test_iterator_constructor(self):
        # constructor by tuple
        self.assertTupleEqual(tuple(self.a2.properties.keys()), DD_ATTRIBUTES)
        # constructor by list
        self.assertListEqual(list(self.a3.properties.keys()), list(DD_ATTRIBUTES))
        # constructor by dict
        self.assertDictEqual(self.a4.properties, ATTRIBUTES_EMPTY)

    def test_getitem(self):
        self.assertEqual(self.a1[STR], None)
        self.assertEqual(self.a2[STR], None)
        self.assertEqual(self.a3[STR], None)
        self.assertEqual(self.a4[STR], None)
        self.assertEqual(self.a5[STR], 5)

    def test_setitem(self):
        self.a5[STR] = 10
        self.assertEqual(self.a5[STR], 10)


if __name__ == '__main__':
    unittest.main()
