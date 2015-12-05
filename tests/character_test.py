import unittest
from characters.character import Character


class CharacterTest(unittest.TestCase):

    def setUp(self):
        self.character = Character(name='Vigor', xp=1000, hp=10)
        self.character_2 = Character(name='Sid', xp=100, hp=1)

    def test_name(self):
        self.assertEqual(self.character.name, 'Vigor')
        self.character.name = 'Chickenleg'
        self.assertEqual(self.character.name, 'Chickenleg')

    def test_xp(self):
        self.assertEqual(self.character.xp, 1000)
        self.character.xp = 5000
        self.assertEqual(self.character.xp, 5000)

    def test_hp(self):
        self.assertEqual(self.character.hp, 10)
        self.character.hp = 15
        self.assertEqual(self.character._hp, 15)

    # methods

    def test_add_xp(self):
        self.character_2.add_xp(xp=5)
        self.assertEqual(self.character_2.xp, 105)

    def test_add_hp(self):
        self.character_2.add_hp(hp=10)
        self.assertEqual(self.character_2.hp, 11)


if __name__ == '__main__':
    unittest.main()
