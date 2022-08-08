from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        player_name = player.username
        usernames = [p.username for p in self.players]

        if player_name in usernames:
            raise ValueError(f'Player {player_name} already exists!')
        self.players.append(player)
        self.count += 1

    def remove(self, player):
        if player == '':
            raise ValueError('Player cannot be an empty string!')
        player_to_remove = [p for p in self.players if p.username == player][0]
        self.players.remove(player_to_remove)
        self.count -= 1

    def find(self, username):
        player_to_find = [p for p in self.players if p.username == username][0]
        return player_to_find
