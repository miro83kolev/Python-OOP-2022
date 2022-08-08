from project.battle_field import Battlefield
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type_p, username):
        if type_p == 'Beginner':
            player = Beginner(username)
        else:
            player = Advanced(username)
        self.player_repository.add(player)
        return f'Successfully added a player of type {type_p} with username: {username}'

    def add_card(self, type_c, name):
        if type_c == 'Magic':
            card = MagicCard(name)
        else:
            card = TrapCard(name)
        self.card_repository.add(card)
        return f'Successfully added card of type {type_c}Card with name: {name}'

    def add_player_card(self, username, card_name):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f'Successfully added card: {card_name} to user: {username}'

    def fight(self, attack_name, enemy_name):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        Battlefield.fight(attacker, enemy)
        return f'Attack user health {attacker.health} - Enemy user health {enemy.health}'

    def report(self):
        result = ''
        for p in self.player_repository.players:
            cards = p.card_repository
            result += f'Username: {p.username} - Health: {p.health} - Cards: {len(cards)}\n'
            for c in cards:
                result += f'### Card: {c.name} - Damage: {c.damage_points}\n'

        return result






