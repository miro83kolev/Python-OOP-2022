from project.core.validator import Validator
from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        # collection of player names
        added_players_names = []
        # iterating thru players args
        for player in players:
            # if player not in self.players collection we add to both collections
            if player not in self.players:
                self.players.append(player)
                added_players_names.append(player.name)
        return f"Successfully added: {', '.join(added_players_names)}"

    def add_supply(self, *supplies):
        # supply could be added more than one time, we iterate thru args supplies
        for supply in supplies:
            self.supplies.append(supply)

    def __find_player_by_name(self, player_name):
        # returns first el of list of players if name is the same as requests in the param of function
        return [player for player in self.players if player.name == player_name][0]

    def sustain(self, player_name, sustenance_type):
        # find a player
        player: Player = self.__find_player_by_name(player_name)
        # checks if player needs sustenance and sustenance type is correct
        if sustenance_type in 'Food Drink' and player is not None:
            if not player.need_sustenance:
                return f'{player_name} have enough stamina.'

        supply: Supply = Validator.check_if_supply_type_is_not_available(self.supplies, sustenance_type)

        try:
            # we try to add energy to players stamina
            player.stamina += supply.energy
        except ValueError:
            # if over 100 Value error and stamina = 100
            player.stamina = 100

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        # we find first player
        first_player = self.__find_player_by_name(first_player_name)
        # we find second player
        second_player = self.__find_player_by_name(second_player_name)
        # we put them in a list
        players = [first_player, second_player]
        output = ""

        # iterates thru that list
        for player in players:
            # if somebody has stamina 0 message below
            if player.stamina == 0:
                output += f"Player {player.name} does not have enough stamina.\n"
        if output:
            return output.strip()

        # we sort them by stamina nas start duel
        players = sorted(players, key=lambda x: x.stamina)
        current_player, next_player = players[0], players[1]
        # for 2 turns
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
        # we go again over the list of players
        for player in self.players:
            try:
                # we try to decrease stamina by age * 2
                player.stamina -= player.age * 2
            except ValueError:
                # if goes below zero it is set to zero
                player.stamina = 0
            # after you try to sustain each player by
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        output = ""
        # for each player
        for player in self.players:
            # use str method from player
            output += str(player) + "\n"
        # for each supply we use details() method
        for supply in self.supplies:
            output += supply.details() + '\n'

        return output.strip()

