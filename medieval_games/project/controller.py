from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        added_players = []
        for player in players:
            if player in self.players:
                continue
            self.players.append(player)
            added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies: Supply):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):

        player = self.__find_player_by_name(player_name)
        if player is None:
            return
        if sustenance_type != 'Food' and sustenance_type != 'Drink':
            return

        idx, supply = self.__find_supply_by_type(sustenance_type)
        if supply is None:
            raise Exception(f'There are no {sustenance_type.lower()} supplies left!')
        if not player.need_sustenance:
            return f'{player_name} have enough stamina.'
        player.stamina = min(player.stamina + supply.energy, 100)
        self.supplies.pop(idx)
        return f'{player_name} sustained successfully with {supply.name}.'

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        err_msg = ''
        if first_player.stamina == 0:
            err_msg += f'Player {first_player.name} does not have enough stamina.'
        if second_player.stamina == 0:
            err_msg += '\n' + f'Player {second_player.name} does not have enough stamina.'
        if err_msg:
            return err_msg.strip()

        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player

        first_player_damage = first_player.stamina / 2
        second_player.stamina = max(second_player.stamina - first_player_damage, 0)
        if second_player.stamina == 0:
            return f'Winner: {first_player.name}'

        second_player_damage = second_player.stamina / 2
        first_player.stamina = max(first_player.stamina - second_player_damage, 0)
        if first_player.stamina == 0:
            return f'Winner: {second_player.name}'

        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f'Winner: {winner.name}'

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        return '\n'.join([str(x) for x in self.players]) + '\n' + \
            '\n'.join([x.details() for x in self.supplies])

    def __find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        return None

    def __find_supply_by_type(self, sustenance_type):
        for idx in range(len(self.supplies) -1, -1, -1):
            supply = self.supplies[idx]
            if supply.__class__.__name__ == sustenance_type:
                return (idx, supply)
        return (-1, None)
