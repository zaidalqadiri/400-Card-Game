import random
from team import Team

def assign_teams(players):
    random_player_1 = random.choice(players)
    players.remove(random_player_1)
    random_player_2 = random.choice(players)
    players.remove(random_player_2)
    random_player_1.set_teammate(random_player_2)
    team1 = Team(random_player_1, random_player_2)

    players[0].set_teammate(players[1])
    team2 = Team(players[0], players[1])

    return random_player_1, random_player_2, players[0], players[1], team1, team2