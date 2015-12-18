import unittest
from rpg_tools.dice import Die

class DieTest(unittest.TestCase):

    def setUp(self):
        self.diecode = Die(code='3d8')
        self.dienumb = Die(casts=4, faces=12)
        self.diesmall = Die(code='1D1')
        self.diebore = Die(code='12d1')

    def test_cast(self):
        self.assertGreaterEqual(self.diecode.cast(), 3)
        self.assertLessEqual(self.diecode.cast(), 24)

        self.assertGreaterEqual(self.dienumb.cast(), 4)
        self.assertLessEqual(self.dienumb.cast(), 48)

        self.assertEqual(self.diesmall.cast(), 1)

        self.assertEqual(self.diebore.cast(), 12)
        self.assertListEqual(self.diebore._sequence,
                             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
