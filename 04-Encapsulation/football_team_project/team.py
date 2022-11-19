from football_team_project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        pass

    def add_player(self, player: Player):
        if player not in self.players:
            self.players.append(player)
            return f"Player {player.name} joined team {self.name}"
        else:
            return f"Player {player.name} has already joined"

    def remove_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                return player
            else:
                return f"Player {player_name} not found"
        else:
            return f"Player {player_name} not found"


"""Sample input: """
p = Player("Pall", 1, 3, 5, 7)

print("Player name:", p.name)
print("Points sprint:", p._Player__sprint)
print("Points dribble:", p._Player__dribble)
print("Points passing:", p._Player__passing)
print("Points shooting:", p._Player__shooting)

print("\ncalling the __str__ method")
print(p)

print("\nAbout the team")
t = Team("Best", 10)
print("Team name:", t._Team__name)
print("Teams points:", t._Team__rating)
print("Teams players:", len(t._Team__players))
print(t.add_player(p))
print(t.add_player(p))
print("Teams players:", len(t._Team__players))
print(t.remove_player("Pall"))
print(t.remove_player("Pall"))

"""Sample output: """
# Player name: Pall
# Points sprint: 1
# Points dribble: 3
# Points passing: 5
# Points shooting: 7
#
# calling the __str__ method
# Player: Pall
# Sprint: 1
# Dribble: 3
# Passing: 5
# Shooting: 7
#
# About the team
# Team name: Best
# Teams points: 10
# Teams players: 0
# Player Pall joined team Best
# Player Pall has already joined
# Teams players: 1
# Player: Pall
# Sprint: 1
# Dribble: 3
# Passing: 5
# Shooting: 7
# Player Pall not found
