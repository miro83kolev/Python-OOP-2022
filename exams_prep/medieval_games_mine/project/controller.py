from project.core.validator import Validator


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(str(player.name))
        return f'Successfully added: {", ".join(added_players)}'

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def __find_player_by_name(self, player_name):
        return [p for p in self.players if p.name == player_name][0]

    def sustain(self, player_name, sustenance_type):
        player = self.__find_player_by_name(player_name)

        if sustenance_type in "Food Drink" and player is not None:
            if not player.need_sustenance:
                return f"{player_name} have enough stamina."

            supply = Validator.raise_if_supply_type_is_not_available(self.supplies, sustenance_type)

            try:
                player.stamina += supply.energy
            except ValueError:
                player.stamina = 100

            return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)
        players = [first_player, second_player]
        output = ""

        for player in players:
            if player.stamina == 0:
                output += f"Player {player.name} does not have enough stamina.\n"
        if output:
            return output.strip()

        players = sorted(players, key=lambda x: x.stamina)
        current_player, next_player = players[0], players[1]

        for turn in range(2):
            try:
                next_player.stamina -= current_player.stamina / 2
            except ValueError:
                next_player.stamina = 0
                break
            current_player, next_player = next_player, current_player

        winner = current_player if current_player > next_player else next_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            try:
                player.stamina -= player.age * 2
            except ValueError:
                player.stamina = 0

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        output = ""
        for player in self.players:
            output += str(player) + "\n"

        for supply in self.supplies:
            output += supply.details() + '\n'

        return output.strip()
