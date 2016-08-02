import unittest
from characters.character import Character, RPGCharacter


class CharacterTest(unittest.TestCase):

    def setUp(self):

        self.c1 = Character()
        self.c2 = Character(name='pippo', xp=1000, hp=25, level=2)
        
        self.rpgc1 = RPGCharacter()
        

    def test_default_character(self):

        self.assertEqual(self.c1.name, 'noname')
        self.assertEqual(self.c1.level, 1)
        self.assertEqual(self.c1.hp, 1)
        self.assertEqual(self.c1.xp, 0)
        # print(self.c1)


    def test_custom_character(self):

        self.assertEqual(self.c2.name, 'pippo')
        self.assertEqual(self.c2.level, 2)
        self.assertEqual(self.c2.hp, 25)
        self.assertEqual(self.c2.xp, 1000)
        # print(self.c2)


    def test_properties(self):

        self.c1.name = 'pluto'
        self.assertEqual(self.c1.name, 'pluto')
        self.c1.level = 10
        self.assertEqual(self.c1.level, 10)
        self.c1.xp = 2000
        self.assertEqual(self.c1.xp, 2000)
        self.c1.hp = 28
        self.assertEqual(self.c1.hp, 28)

        
    def test_default_RPGCharacter(self):
        
        self.assertEqual(self.rpgc1.name, 'noname')
        self.assertEqual(self.rpgc1.level, 1)
        self.assertEqual(self.rpgc1.hp, 1)
        self.assertEqual(self.rpgc1.xp, 0)
        # print(self.rpgc1)
        




if __name__ == '__main__':
    unittest.main()
