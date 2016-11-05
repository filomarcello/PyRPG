import unittest

from environment.map import Map
from environment.tile import Tile


class TestTile(unittest.TestCase):

    def setUp(self):
        self.t1 = Tile()
        self.t2 = Tile(terrain='grass', view='G')

    def test_view(self):
        self.assertEqual(self.t1.view, None)
        self.assertEqual(self.t2.view, 'G')

class TestMap(unittest.TestCase):

    def setUp(self):

        self.t1 = Tile()
        self.t2 = Tile(view='2')
        self.t3 = Tile(view='3')

        self.tile_grid1 = [[self.t1] * 10 for i in range(11)]
        self.tile_grid2 = [[self.t2] * 3, [self.t3] * 3,
                           [self.t2, self.t3, self.t2]]

        self.m1 = Map(tiles=self.tile_grid1, name='map1',
                      info='made of the same Tile repeated for 110 times')

        self.m2 = Map(tiles=self.tile_grid2)

    def test_dimensions(self):
        self.assertTupleEqual(self.m1._dim, (11, 10))

    def test_tile(self):
        self.assertEqual(self.m1.get_tile(1, 1), self.t1)

        # test view property on Tile obtained by Map.get_tile
        self.assertEqual(self.m1.get_tile(1, 1).view, None)

    def test_view(self):
        self.assertListEqual(self.m1.view(2, 2, 5, 5),
                             [[self.t1.view] * 4 for i in range(4)])

        self.assertListEqual(self.m1.view_all(), [[None] * 10] * 11)
        self.assertListEqual(self.m2.view_all(), [['2', '2', '2'],
                                                  ['3', '3', '3'],
                                                  ['2', '3', '2']])

    # TODO: get_tile


if __name__ == '__main__':
    unittest.main()
