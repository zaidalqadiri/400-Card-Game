"""
This module contains a utility function to randomly assign four players into two teams.
It uses the Team class to group players and sets their teammates accordingly.
"""

import random
from team import Team

def assign_teams(players):
    """
    Randomly assigns four players into two teams.

    The function:
    - Randomly selects two players and forms the first team.
    - Forms the second team with the remaining two players.
    - Sets each player's teammate using the `set_teammate` method.

    Args:
        players (list[Player]): A list of four Player objects.

    Returns:
        tuple: A tuple containing:
            - random_player_1 (Player)
            - random_player_2 (Player)
            - player3 (Player)
            - player4 (Player)
            - team1 (Team)
            - team2 (Team)
    """
    random_player_1 = random.choice(players)
    players.remove(random_player_1)
    random_player_2 = random.choice(players)
    players.remove(random_player_2)
    random_player_1.set_teammate(random_player_2)
    team1 = Team(random_player_1, random_player_2)

    players[0].set_teammate(players[1])
    team2 = Team(players[0], players[1])

    return random_player_1, random_player_2, players[0], players[1], team1, team2