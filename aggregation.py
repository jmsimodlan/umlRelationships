class Player:
    def __init__(self, name):
        self.name = name


class Team:
    def __init__(self, players):
        # Players are passed in from outside
        self.players = players

    def show_players(self):
        print("Team players:")
        for player in self.players:
            print(player.name)


# Create players independently
player1 = Player("Alex")
player2 = Player("Jordan")

# Pass the existing players to the team
team = Team([player1, player2])

# Display the players
team.show_players()
