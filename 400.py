import random

class Card:
    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank

    def __str__(self):
        return f"{self.__rank} of {self.__suit}"
    
class Deck:
    def __init__(self):
        suits = ['Diamond', 'Heart', 'Spade', 'Club']
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

        self.__deck = []

        for suit in suit:
            for rank in ranks:
                self.__deck.append(Card(suit, rank))

        random.shuffle(self.__deck)
    
    def deal(player):
        pass

class Player:
    def __init__(self, name):
        self.__name = name
        self.__cards = []
        self.__bid = None
        self.__score = 0
        self.__tricks = 0
        self.__team = None
    
    def make_bid(self, amount):
        if amount < 2:
            print("The minimum bid is 2")
        elif amount == 2 and self.__score >= 30:
            print("The minimum bid for a score of 30 and above is 3")
        elif amount == 3 and self.__score >= 40:
            print("The minimum bid for a score of 40 and above is 4")
        else:
            self.__bid = amount
            return self.__bid
    
    def play_card(self, card):
        pass

class Team:
    _team_count = 0

    def __init__(self, player1, player2):
        self.__players = [player1, player2]
        Team._team_count += 1
        self.__team_id = Team._team_count
    
    def get_team_info(self):
        return f"Team {self.__team_id}: {self.__players[0]} and {self.__players[1]}"

class Game:

    _current_round = 0

    def __init__(self, player1, player2, player3, player4, team1, team2):
        self.__players = [player1, player2, player3, player4]
        self.__deck = Deck().__deck
        self.__teams = [team1, team2]

    def start_game():
        pass
    
    def bid_phase():
        pass

    def play_round():
        pass

    def evaluate_tricks():
        pass 
