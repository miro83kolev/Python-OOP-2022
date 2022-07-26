from unittest import TestCase, main

from hero.project.hero import Hero


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Warrior", 10, 100, 50)
        self.enemy = Hero("Attacker", 10, 100, 50)
    def test_hero_init(self):
        username = 'Warrior'
        level = 10
        health = 100
        damage = 50

        hero = Hero(username, level, health, damage)

        self.assertEqual(username, hero.username)
        self.assertEqual(level, hero.level)
        self.assertEqual(health, hero.health)
        self.assertEqual(damage, hero.damage)


    def test_str_returns_correct_result(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        actual_result = str(self.hero)
        self.assertEqual(expected_result, actual_result)

    def test_battle_raises_when_hero_attacks_himself(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.hero)
        self.assertEqual('You cannot fight yourself', str(context.exception))

    def test_battle_raises_when_hero_is_dead(self):
        for health in [0, -50]:
            self.hero.health = health

            with self.assertRaises(Exception) as context:
                self.hero.battle(self.enemy)
            self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(context.exception))

    def test_battle_raises_when_enemy_is_dead(self):
        for health in [0, -50]:
            self.enemy.health = health

            with self.assertRaises(Exception) as context:
                self.hero.battle(self.enemy)
            self.assertEqual(f'You cannot fight {self.enemy.username}. He needs to rest', str(context.exception))

    def test_battle_returns_draw_both_heroes_dead(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual('Draw', result)
        self.assertEqual(-400, self.hero.health)
        self.assertEqual(-400, self.enemy.health)

    def test_battle_returns_win_for_hero(self):
        enemy = Hero("Attacker", 1, 100, 50)

        expected_level = self.hero.level + 1
        result = self.hero.battle(enemy)

        self.assertEqual('You win', result)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(55, self.hero.damage)
        self.assertEqual(-400, enemy.health)

    def test_battle_returns_loose_for_hero(self):
        hero = Hero('Warrior', 1, 100, 50)
        enemy = Hero('Attacker', 1, 100, 50)

        result = hero.battle(enemy)

        self.assertEqual('You lose', result)
        self.assertEqual(2, enemy.level)
        self.assertEqual(55, enemy.health)
        self.assertEqual(55, enemy.damage)
        self.assertEqual(50, hero.health)


if __name__ == '__main__':
    main()