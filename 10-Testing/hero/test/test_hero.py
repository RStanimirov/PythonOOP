# RS solution 81/100 :
import unittest

from hero.project.hero import Hero
# from project.hero import Hero


class TestHero(unittest.TestCase):
    def test_init(self):
        hero = Hero("Gawain", 12, 100.0, 3.0)
        self.assertEqual("Gawain", hero.username)
        self.assertEqual(12, hero.level)
        self.assertEqual(100.0, hero.health)
        self.assertEqual(3.0, hero.damage)

    def test_battle_with_self_raise_Exception(self):
        hero = Hero("Gawain", 12, 100.0, 3.0)
        enemy_hero = Hero("Gawain", 12, 100.0, 3.0)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_no_self_health_raise_ValueError(self):
        hero = Hero("Gawain", 12, -1.0, 3.0)
        enemy = Hero("Diablo", 20, 100.0, 4.0)
        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_with_no_health_raise_ValueError(self):
        hero = Hero("Gawain", 12, 80.0, 3.0)
        enemy = Hero("Diablo", 20, -1.0, 4.0)
        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)
        self.assertEqual("You cannot fight Diablo. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        hero = Hero("Gawain", 12, 30.0, 3.0)
        enemy = Hero("Diablo", 20, 10.0, 4.0)
        result = hero.battle(enemy)
        self.assertEqual("Draw", result)

    def test_battle_win(self):
        hero = Hero("Gawain", 12, 100.0, 3.0)
        enemy = Hero("Diablo", 20, 20.0, 4.0)
        result = hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(hero.level, 13)
        self.assertEqual(hero.health, 25.0)
        self.assertEqual(hero.damage, 8.0)

    def test_battle_lose(self):
        hero = Hero("Gawain", 12, 80.0, 3.0)
        enemy = Hero("Diablo", 20, 50.0, 4.0)
        result = hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(enemy.level, 21)
        self.assertEqual(enemy.health, 19.0)
        self.assertEqual(enemy.damage, 9.0)

    def test_str(self):
        hero = Hero("Gawain", 12, 100.0, 3.0)
        expected_str = f"Hero Gawain: 12 lvl\nHealth: 100.0\nDamage: 3.0\n"
        actual_str = hero.__str__()
        self.assertEqual(expected_str, actual_str)


if __name__ == '__main__':
    unittest.main()
