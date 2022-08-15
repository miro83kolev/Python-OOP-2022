from collections import deque
class System:

    # finding by name something in a collection /might be used for items, names etc
    @staticmethod
    def find_instance_by_name(name, collection):
        for instance in collection:
            if instance.name == name:
                return instance
        return None

    # instance method to find name in a collection
    def find_by_name(self, name: str):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
        return None

    # static method using deque from 0 to 5 elements in list
    @staticmethod
    def explore_planet(astronauts, planet):
        astronauts = deque(astronauts[:5])
        items = planet.items
        astronauts_count = 1

        while items and astronauts:
            current_astronaut = astronauts[0]
            current_item = items.pop()

            current_astronaut.breathe()
            current_astronaut.backpack.append(current_item)
            if current_astronaut.oxygen <= 0:
                astronauts.popleft()
                astronauts_count += 1

        if items:
            SpaceStation.not_successful_missions += 1 # class attr
            return "Mission is not completed."

        SpaceStation.successful_missions += 1 # class attr
        return f"Planet: {planet.name} was explored. {astronauts_count} astronauts participated in collecting items."

    # find user by name in users collection
    def __find_user_by_username(self, username):
        return [user for user in self.users_collection if user.username == username][0]

    # when players take turn using 2 players
    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.find_player_by_name(first_player_name)
        second_player = self.find_player_by_name(second_player_name)
        players = [first_player, second_player]
        output = ""

        for player in players:
            if player.stamina == 0:
                output += f"Player {player.name} does not have enough stamina.\n"
        if output:
            return output.strip()

        players = sorted(players, key=lambda x: x.stamina) # players sorted by their stamina
        current_player, next_player = players[0], players[1]

        for turn in range(2): # 2 turns
            try:
                next_player.stamina -= current_player.stamina / 2
            except ValueError:
                next_player.stamina = 0
                break
            current_player, next_player = next_player, current_player

        winner = current_player if current_player > next_player else next_player
        return f"Winner: {winner.name}"

    # checks with try except
    def next_day(self):
        for player in self.players:
            try:
                player.stamina -= player.age * 2
            except ValueError:
                player.stamina = 0

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    # checks with try except condition
    def sustain(self, player_name: str, sustenance_type: str):
        player: Player = self.find_player_by_name(player_name) # creates a player

        if sustenance_type in "Food Drink" and player is not None: # if player is not none and type is ok
            if not player.need_sustenance:
                return f"{player_name} have enough stamina."

            supply: Supply = Validator.raise_if_supply_type_is_not_available(self.supplies, sustenance_type) # supply creation

            try:
                player.stamina += supply.energy
            except ValueError:
                player.stamina = 100

            return f"{player_name} sustained successfully with {supply.name}."
