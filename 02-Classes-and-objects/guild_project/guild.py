from guild_project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player):
        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.list_of_players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        if self.list_of_players:
            for x in self.list_of_players:
                if x.name == player_name:
                    x.guild = "Unaffiliated"
                    self.list_of_players.remove(x)
                    return f"Player {player_name} has been removed from the guild."
                else:
                    return f"Player {player_name} is not in the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for x in self.list_of_players:
            result += x.player_info()
        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
