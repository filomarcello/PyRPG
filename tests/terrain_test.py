import unittest
from environment.terrains import Terrain

imag1 = 'G'
imag2 = 'g'

class TerrainTest(unittest.TestCase):

    def setUp(self):
        self.terr = Terrain(name='grass', image=imag1)
        self.terr2 = Terrain(name='high mountain', a_locked=False,
                             u_locked=True, g_locked=True)

    def test_image(self):

        self.assertEqual(self.terr.image, imag1)
        self.terr.image = imag2
        self.assertEqual(self.terr.image, imag2)

    def test_locked(self):

        self.assertFalse(self.terr2.a_locked)
        self.assertTrue(self.terr2.u_locked)
        self.assertTrue(self.terr2.g_locked)


if __name__ == '__main__':
    unittest.main()
