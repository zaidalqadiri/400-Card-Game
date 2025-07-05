"""
team.py

This module defines the Team class used to represent a team of two players 
in a card game. Each team is assigned a unique team ID upon creation.

Classes:
    Team: Represents a team consisting of two player objects.
"""

class Team:
    """
    Represents a team consisting of two players.

    Class Attributes:
        _team_count (int): A class-level counter to assign unique team IDs.

    Instance Attributes:
        __players (list): A list containing two player objects.
        __team_id (int): Unique identifier for the team.
    """
    _team_count = 0

    def __init__(self, player1, player2):
        """
        Initializes a Team with two player objects and assigns a unique team ID.

        Args:
            player1 (Player): The first player in the team.
            player2 (Player): The second player in the team.
        """
        self.__players = [player1, player2]
        Team._team_count += 1
        self.__team_id = Team._team_count
    
    def get_team_info(self):
        """
        Returns a string representation of the team with player names.

        Returns:
            str: A string like "Team 1: Alice and Bob".
        """
        return f"Team {self.__team_id}: {self.__players[0].get_name()} and {self.__players[1].get_name()}"