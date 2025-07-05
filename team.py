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
        self.__players = [player1, player2]
        Team._team_count += 1
        self.__team_id = Team._team_count
    
    def get_team_info(self):
        return f"Team {self.__team_id}: {self.__players[0].get_name()} and {self.__players[1].get_name()}"